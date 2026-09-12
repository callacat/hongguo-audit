#!/usr/bin/env python3
# HG-1：硬编码网络端点提取 + 番茄壳端点集比对（漂移项单列）
# 输入：
#   work/smali-hg-mod/**/*.smali        —— 红果外层全部类（含官方挪入类，用于壳端点初筛）
#   work/added-classes.txt              —— 真新增类名清单（壳端点候选主集）
#   work/overlap-classes.txt            —— 与番茄画像重合（A 类）
#   work/fanqie/fq-mod/**/*.dex         —— 番茄 16a 壳外层 dex（同 regex 现扫，画像端点集）
# 输出：work/diff-out/docs/hg1-endpoints.md
import os, re, sys
from collections import defaultdict

work = sys.argv[1]
HG_SMALI = os.path.join(work, 'smali-hg-mod')
HG_ADD = os.path.join(work, 'added-classes.txt')
HG_OVL = os.path.join(work, 'overlap-classes.txt')
FQ_DIR = os.path.join(work, 'fanqie', 'fq-mod')
OUT = os.path.join(work, 'diff-out', 'docs', 'hg1-endpoints.md')

STR_RE = re.compile(r'^\s*const-string(?:/16|/jumbo)?\s+v\d+,\s*"((?:[^"\\]|\\.)*)"\s*$')
URL_RE = re.compile(r'https?://[a-zA-Z0-9_\-./:%~#?&=]+')
IP_RE = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
DOM_RE = re.compile(r'\b[a-zA-Z0-9][a-zA-Z0-9\-]{0,60}(?:\.[a-zA-Z0-9][a-zA-Z0-9\-]{0,60})+\.[a-zA-Z]{2,}\b')

def norm_url(u):
    u = u.rstrip('./:').lower()
    return u

def norm_domain(d):
    return d.lower().strip('.')

BAD_HOSTS = re.compile(
    r'\.(?:xml|w3\.org|apache\.org|purl\.org|json-schema\.org|slf4j\.org|javase|java\.oracle|android\.com|'
    r'gnu\.org|mozilla\.org|schema|example|localhost|githubusercontent)$|'
    r'^java|^javax|^sun\.|^com/sun|^android/|^dalvik|^kotlin|^org/xml|^org/w3|^org/apache', re.I)
BAD_DOM = re.compile(r'^java|^javax|^sun|^dalvik|^kotlin|^android|^org$|^com$', re.I)

def hits_from_string(s):
    urls = set(norm_url(m) for m in URL_RE.findall(s))
    urls = {u for u in urls if not BAD_HOSTS.search(u.split('://')[-1].split('/')[0] if '://' in u else u)}
    ips = set(m for m in IP_RE.findall(s) if not re.match(r'^(0\.|127\.|25[5-9]\.|2[6-9]\.|[3-9]\d?\.)', m))
    doms = set()
    if not urls:
        for d in DOM_RE.findall(s):
            nd = norm_domain(d)
            if BAD_DOM.search(nd) or BAD_HOSTS.search(nd):
                continue
            if '.' in nd and not nd[0].isdigit():
                doms.add(nd)
    return urls, ips, doms

def scan_smali(path):
    urls, ips, doms = set(), set(), set()
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            m = STR_RE.match(line.rstrip('\n'))
            if not m:
                continue
            s = m.group(1)
            u, i, d = hits_from_string(s)
            urls |= u; ips |= i; doms |= d
    return urls, ips, doms

def scan_dex(path):
    data = open(path, 'rb').read()
    text = data.decode('latin-1')
    urls, ips, doms = set(), set(), set()
    for seg in re.findall(r'[\x20-\x7e]{6,}', text):
        u, i, d = hits_from_string(seg)
        urls |= u; ips |= i; doms |= d
    return urls, ips, doms

hg_added = set(l.strip() for l in open(HG_ADD, encoding='utf-8') if l.strip())
hg_overlap = set(l.strip() for l in open(HG_OVL, encoding='utf-8') if l.strip())

def norm(k):
    stem = k[:-6] if k.endswith('.smali') else k
    return stem.split('$')[0]

hg_overlap_n = {norm(k) for k in hg_overlap}

# 1) 红果全量端点（按类），分：新增且重合(A壳候选) / 新增不重合(B/C/D) / 官方既有(信息项)
url_by_class = defaultdict(set)
ip_by_class = defaultdict(set)
dom_by_class = defaultdict(set)
stats = {'total': 0, 'added': 0, 'official': 0}
for droot, _, fs in os.walk(HG_SMALI):
    for f in fs:
        if not f.endswith('.smali'):
            continue
        rel = os.path.relpath(os.path.join(droot, f), HG_SMALI)
        key = '/'.join(rel.split(os.sep)[1:]) if os.sep in rel else rel
        u, i, d = scan_smali(os.path.join(droot, f))
        if u or i or d:
            url_by_class[key] |= u
            ip_by_class[key] |= i
            dom_by_class[key] |= d
        stats['total'] += 1
        if key in hg_added:
            stats['added'] += 1
        else:
            stats['official'] += 1

def cls_kind(key):
    nk = norm(key)
    if key in hg_added:
        return 'A' if nk in hg_overlap_n else 'BCD'
    return 'OFF'

# 2) 番茄壳端点集 = 新增类∩画像重合（A 类，16a 已定性的壳代码）+ 全部新增类（宽口径对照）
fq_urls, fq_ips, fq_doms = set(), set(), set()
fq_cls = 0
for root, _, fs in os.walk(FQ_DIR):
    for f in fs:
        if f.endswith('.dex'):
            u, i, d = scan_dex(os.path.join(root, f))
            fq_urls |= u; fq_ips |= i; fq_doms |= d
            fq_cls += 1

hg_urls, hg_ips, hg_doms = set(), set(), set()
for key in hg_added:
    nk = norm(key)
    if nk in hg_overlap_n:
        hg_urls |= url_by_class.get(key, set())
        hg_ips |= ip_by_class.get(key, set())
        hg_doms |= dom_by_class.get(key, set())

fq_urls -= {u for u in fq_urls if 'github.com' in u or 'githubusercontent' in u}
fq_doms -= {'github.com', 'githubusercontent.com', 'actions.githubusercontent.com'}
hg_urls -= {u for u in hg_urls if 'github.com' in u or 'githubusercontent' in u}
hg_doms -= {'github.com', 'githubusercontent.com'}

drift_urls = hg_urls - fq_urls
drift_ips = hg_ips - fq_ips
drift_doms = hg_doms - fq_doms

L = []
L.append('# HG-1 外层硬编码网络端点清单')
L.append('')
L.append('> 方法：baksmali const-string 全量扫描（红果）+ dex 字符串区 regex（番茄壳，同口径正则）。')
L.append('> 端点集定义：红果端点=真新增类∩画像重合（A 壳）；漂移项=红果壳端点−番茄壳端点。')
L.append('> 已知局限：dex 级扫描含字符串交叉碎片，URL 已去重清洗、滤掉 java/android/org 等 schema 噪声与 github CI 自引。')
L.append('')
L.append(f'- 红果外层扫描类文件数: {stats["total"]}（真新增 {stats["added"]} / 官方既有 {stats["official"]}，官方端点为信息项不计入壳漂移）')
L.append(f'- 番茄壳: 16a 外层 {fq_cls} 个 dex 全量扫描')
L.append('')

L.append('## 1. 红果壳端点（A 类=与番茄画像重合壳类）')
L.append('')
L.append('### URL')
for u in sorted(hg_urls):
    L.append(f'- `{u}`')
L.append('')
L.append('### IP')
for u in sorted(hg_ips):
    L.append(f'- `{u}`')
L.append('')
L.append('### 域名')
for u in sorted(hg_doms):
    L.append(f'- `{u}`')
L.append('')

L.append('## 2. 番茄壳端点（16a 基线，dex 现扫）')
L.append('')
L.append('### URL')
for u in sorted(fq_urls):
    L.append(f'- `{u}`')
L.append('')
L.append('### IP')
for u in sorted(fq_ips):
    L.append(f'- `{u}`')
L.append('')
L.append('### 域名')
for u in sorted(fq_doms):
    L.append(f'- `{u}`')
L.append('')

RED = (len(drift_urls) + len(drift_doms)) > max(10, len(hg_urls)) * 0.5
L.append('## 3. 漂移项（红果壳有、番茄壳无）' + (' 🚩大漂移——重合端点占比过低' if RED else ''))
L.append('')
L.append(f'漂移规模: URL {len(drift_urls)} 项 / IP {len(drift_ips)} 项 / 域名 {len(drift_doms)} 项（红果壳全集 URL {len(hg_urls)} / IP {len(hg_ips)} / 域名 {len(hg_doms)}）')
L.append('')
L.append('### 漂移 URL')
for u in sorted(drift_urls):
    L.append(f'- `{u}`')
L.append('')
L.append('### 漂移 IP')
for u in sorted(drift_ips):
    L.append(f'- `{u}`')
L.append('')
L.append('### 漂移域名')
for u in sorted(drift_doms):
    L.append(f'- `{u}`')
L.append('')

L.append('## 4. 红果真新增·不重合类（B/C/D 候选）端点明细')
L.append('')
L.append('（若此类带端点→C 类重点；无端点列空表=壳外新增类未硬编码网络出口，B/D 倾向）')
L.append('')
L.append('| 类 | 类型 | URL | 域名 | IP |')
L.append('|---|---|---|---|---|')
rows = 0
for key in sorted(hg_added):
    nk = norm(key)
    if nk in hg_overlap_n:
        continue
    u = url_by_class.get(key, set())
    i = ip_by_class.get(key, set())
    d = dom_by_class.get(key, set())
    if u or i or d:
        rows += 1
        L.append(f'| `{key}` | BCD | {" ".join(f"`{x}`" for x in sorted(u))} | {" ".join(f"`{x}`" for x in sorted(d))} | {" ".join(f"`{x}`" for x in sorted(i))} |')
L.append('')
L.append(f'（有端点的 BCD 候选类: {rows} / BCD 候选总数: {len([k for k in hg_added if norm(k) not in hg_overlap_n])}）')
L.append('')

L.append('## 5. 官方既有类端点（信息项，红果外层中的官方代码）')
L.append('')
off_urls = defaultdict(set)
for key, u in url_by_class.items():
    if key not in hg_added:
        for x in u:
            off_urls[x].add(key)
top_off = sorted(off_urls.items(), key=lambda kv: -len(kv[1]))[:40]
L.append(f'- 官方类携带去重 URL 总数: {len(off_urls)}（列 top40 出现类频次）')
L.append('')
for x, c in top_off:
    L.append(f'- `{x}`（{len(c)} 类）')
L.append('')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(L))

print(f'HG1-EP hgA urls={len(hg_urls)} ips={len(hg_ips)} doms={len(hg_doms)} | fq urls={len(fq_urls)} ips={len(fq_ips)} doms={len(fq_doms)} | drift urls={len(drift_urls)} doms={len(drift_doms)} red={RED}')
print(f'HG1-EP BCD-with-endpoints={rows} official-urls={len(off_urls)}')

#!/usr/bin/env python3
# HG-3：com/b/a C 类后门家族存续点位复扫（只读扫描，不改写任何文件——净化是后续轮的活）
# v7.3.6.32 基线（HG-1 终判 + HG-2 实测 docs/hg2-patch.log）：
#   家族 3 类（a / a$Android_id / a$Reflect）、外部 invoke 1 点位
#   （MuteApplication.onCreate → init()V）、家族自引用文件 2、官方内层引用 0。
# 口径与 HG-2 一致：家族本体 = 路径段 …/com/b/…（本体自引用豁免）；
#   外部 = com/b 之外对 Lcom/b/a; 的引用（invoke 与非 invoke 指令分列）。
# 输入：work/smali-hg-mod/、work/smali-hg-inner/（baksmali 每 dex 一子目录）
# 输出：work/diff-out/docs/{TAG}-diff-report.md 附 §8；机器行 HG3-C
import os, re, sys

work = sys.argv[1]
TAG = os.environ.get('HG_TAG', 'hg3')
VER = os.environ.get('HG_VER', 'v7.3.7.32')
MOD = os.path.join(work, 'smali-hg-mod')
INN = os.path.join(work, 'smali-hg-inner')
REPORT = os.path.join(work, 'diff-out', 'docs', f'{TAG}-diff-report.md')

TARGET = 'Lcom/b/a;'
INVOKE_RE = re.compile(r'invoke-(static|virtual|super|direct|interface)(/range)?\s+\{([^}]*)\},\s*'
                       + re.escape(TARGET) + r'->([\w$<>]+)\(([^)]*)\)(\S+)')
METHOD_RE = re.compile(r'^\.method\b')

BASELINE = {'family': {'com/b/a', 'com/b/a$Android_id', 'com/b/a$Reflect'},
            'ext_files': 1, 'ext_invokes': 1, 'internal_ref_files': 2, 'inner_hits': 0}
CHAIN_METHODS = ['init', 'getApplication', 'getID', 'getReflect', 'onCreate']
MARKERS = ['deviceid', 'ANDROID_ID', 'Settings$Secure', 'ActivityThread', 'currentApplication',
           'android_id', 'getDeviceId', 'Bluetooth']

def walk_smali(root):
    for droot, _, fs in os.walk(root):
        for f in fs:
            if f.endswith('.smali'):
                p = os.path.join(droot, f)
                yield p, os.path.relpath(p, root)

def is_family(rel):
    parts = rel.split(os.sep)
    return len(parts) >= 3 and parts[-3] == 'com' and parts[-2] == 'b'

def cls_key(rel):
    parts = rel.split(os.sep)
    stem = parts[-1][:-6]
    return '/'.join(parts[1:-1] + [stem])

# ---- 家族清单（mod 内）----
family = {}          # key -> {'methods':[], 'markers':{}}
for p, rel in walk_smali(MOD):
    if not is_family(rel):
        continue
    txt = open(p, encoding='utf-8', errors='replace').read()
    methods = re.findall(r'^\.method\s+.*?([a-zA-Z$][\w$]*)\(', txt, re.M)
    marks = {m: txt.count(m) for m in MARKERS if m in txt}
    family[cls_key(rel)] = {'methods': sorted(set(methods)), 'markers': marks}

# ---- 外部/内部引用扫描（mod 全树）----
ext_hits = []        # (file_rel, caller_method, invoke文本)
ext_noninvoke = []   # (file_rel, 指令行) 含 Lcom/b/a; 但非 invoke 行
ext_dotstr = []      # (file_rel, 行) 字符串点分形态 "com.b.a"
internal_ref_files = 0
DOT_RE = re.compile(r'"com\.b\.a')
for p, rel in walk_smali(MOD):
    txt = open(p, encoding='utf-8', errors='replace').read()
    if is_family(rel):
        # 家族本体：只统计自引用文件数（HG-2 同款豁免，入口断后永不执行）
        if TARGET in txt:
            internal_ref_files += 1
        continue
    if TARGET not in txt and not DOT_RE.search(txt):
        continue
    cur_m = ''
    for ln in txt.split('\n'):
        if METHOD_RE.match(ln):
            cur_m = ln.strip()[:90]
        if TARGET in ln:
            m = INVOKE_RE.search(ln)
            if m:
                ext_hits.append((rel, cur_m, ln.strip()[:140]))
            else:
                ext_noninvoke.append((rel, cur_m, ln.strip()[:140]))
        elif DOT_RE.search(ln):
            ext_dotstr.append((rel, ln.strip()[:100]))

# ---- 官方内层引用（必须 0，非 0 = 内层包本身带链，红旗）----
inner_hits = 0
inner_family = 0
for p, rel in walk_smali(INN):
    if is_family(rel):
        inner_family += 1
    if TARGET in open(p, encoding='utf-8', errors='replace').read():
        inner_hits += 1

# ---- 报告 §8 ----
L = ['', f'## 8. com/b/a C 类家族存续点位复扫（{VER}，只读）', '']
L.append('> 口径=HG-2 invoke-NOP 同款（com/b/ 本体自引用豁免）。判定权在老马：本节仅列存续事实。')
L.append('')
L.append(f'### 家族类清单（{len(family)} 类；v736 基线 3 类）')
L.append('')
L.append('| 类 | .method 数 | 含关键链方法 | 特征字符串命中 |')
L.append('|---|---|---|---|')
for k in sorted(family):
    v = family[k]
    chain = ' '.join(m for m in CHAIN_METHODS if any(mm == m or mm.endswith('$' + m) for mm in v['methods'])) or '-'
    marks = ' '.join(f'{m}×{c}' for m, c in sorted(v['markers'].items())) or '-'
    L.append(f'| `{k}` | {len(v["methods"])} | {chain} | {marks} |')
gone = sorted(BASELINE['family'] - set(family))
newf = sorted(set(family) - BASELINE['family'])
L.append('')
L.append(f'- 基线类缺失（v736 有 v737 无）: {gone if gone else "无"}')
L.append(f'- 家族新增成员（v736 无 v737 有）: {newf if newf else "无"}')
L.append('')
L.append(f'### 外部 invoke 点位（com/b 之外 → {TARGET}）：{len(ext_hits)} 条 / {len(set(h[0] for h in ext_hits))} 文件（v736 基线 1 点位）')
L.append('')
if ext_hits:
    L.append('| 文件 | 所在 .method | 指令 |')
    L.append('|---|---|---|')
    for rel, m, ln in sorted(ext_hits):
        L.append(f'| `{rel}` | `{m}` | `{ln}` |')
else:
    L.append('（无——后门入口链在该版本断裂）')
L.append('')
L.append(f'### 非 invoke 引用（字段/类型引用等，信息项）：{len(ext_noninvoke)} 条')
for rel, m, ln in sorted(ext_noninvoke)[:20]:
    L.append(f'- `{rel}` `{m}` → `{ln}`')
L.append('')
L.append(f'### 点分字符串形态（"com.b.a"，反射/Class.forName 面，信息项）：{len(ext_dotstr)} 条')
for rel, ln in sorted(set(ext_dotstr))[:20]:
    L.append(f'- `{rel}` → `{ln}`')
L.append('')
L.append(f'- 家族本体自引用文件数: {internal_ref_files}（v736 基线 2，豁免不参与计数）')
L.append(f'- **官方内层引用 {TARGET} 的文件数: {inner_hits}；内层 com/b/ 路径类文件: {inner_family}（两者必须=0，非 0=内层官方包本身带链，重大红旗）**')
L.append('')

os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, 'a', encoding='utf-8') as f:
    f.write('\n'.join(L))

print(f'HG3-C family_classes={len(family)} ext_files={len(set(h[0] for h in ext_hits))} '
      f'ext_invokes={len(ext_hits)} noninvoke_lines={len(ext_noninvoke)} dotstr_lines={len(ext_dotstr)} '
      f'internal_ref_files={internal_ref_files} inner_hits={inner_hits} inner_family={inner_family}')
print(f'HG3-C BASELINE family_gone={gone or "-"} family_new={newf or "-"} '
      f'v736(ext_files=1,ext_invokes=1,internal_ref_files=2,inner_hits=0)')
if ext_noninvoke or ext_dotstr:
    print(f'HG3-C WATCH 非invoke/点分引用>0，调用形态可能超出口径，列 §8 供老马归案')
if inner_hits or inner_family:
    print(f'HG3-C REDFLAG 官方内层出现 com/b/a 引用!!')

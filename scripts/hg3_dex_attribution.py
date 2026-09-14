#!/usr/bin/env python3
# HG-3：外层 dex 归属分析——「壳多出的 dex」（如 classes24.dex）= 真新增类 还是 官方类重排？
# 原理：类名对齐后，某 mod dex 内的类分两堆：
#   added=不在内层官方包（真新增，hg1_diff 同口径）；official=在内层存在。
#   official 再分：内层同名 dex（classesN 对 classesN）就地保留 vs 挪位（内层来自其他 dex）。
#   纯重排堆dex：added≈0 且 official 几乎全为挪位 → 打包器 dex 追加/重排；
#   真新增堆dex：added 占比高 → 作者在该 dex 注入新代码。
# 输入：work/smali-hg-mod、work/smali-hg-inner、work/added-classes.txt
# 输出：work/diff-out/docs/{TAG}-diff-report.md 附 §9；机器行 HG3-DEX
import os, sys
from collections import Counter

work = sys.argv[1]
TAG = os.environ.get('HG_TAG', 'hg3')
VER = os.environ.get('HG_VER', 'v7.3.7.32')
MOD = os.path.join(work, 'smali-hg-mod')
INN = os.path.join(work, 'smali-hg-inner')
ADDED = os.path.join(work, 'added-classes.txt')
REPORT = os.path.join(work, 'diff-out', 'docs', f'{TAG}-diff-report.md')

def dex_index(root):
    """dex子目录名 -> 类key集合（key=去 dex 前缀去 .smali）；另返回全量 key->dex 首现映射。"""
    per, first = {}, {}
    for d in sorted(os.listdir(root)):
        dp = os.path.join(root, d)
        if not os.path.isdir(dp):
            continue
        s = set()
        for droot, _, fs in os.walk(dp):
            for f in fs:
                if not f.endswith('.smali'):
                    continue
                key = os.path.relpath(os.path.join(droot, f), dp)[:-6]
                s.add(key)
                first.setdefault(key, d)
        per[d] = s
    return per, first

mod_per, _ = dex_index(MOD)
inn_per, inn_first = dex_index(INN)
added = set()
with open(ADDED, encoding='utf-8') as f:
    for ln in f:
        ln = ln.strip()
        if ln:
            added.add(ln[:-6] if ln.endswith('.smali') else ln)

inn_names = set(inn_per)
mod_names = set(mod_per)
extra = sorted(mod_names - inn_names)
missing = sorted(inn_names - mod_names)

L = ['', f'## 9. 外层 dex 归属分析（{VER}：壳 dex vs 官方 dex）', '']
L.append('> 判据：类名对齐（同 §1 口径）。重排堆dex=added≈0 且 official 全为挪位；注入堆dex=added 占比高。判定权在老马。')
L.append('')
L.append(f'- 外层 dex: {len(mod_per)} 个 ｜ 内层官方 dex: {len(inn_per)} 个 ｜ 外层独有 dex 名: {", ".join("`"+d+"`" for d in extra) if extra else "无"} ｜ 内层独有（壳未带）: {", ".join(missing) if missing else "无"}')
L.append('')
L.append('| 外层dex | 类总数 | 真新增 | 官方就地¹ | 官方挪位² | 新增占比 |')
L.append('|---|---|---|---|---|---|')
moved_total = 0

def dex_sort(x):
    suf = x[7:] if x.startswith('classes') else ''
    return (0, 0) if x == 'classes' else (int(suf), 0) if suf.isdigit() else (999, 0)

for d in sorted(mod_per, key=dex_sort):
    ks = mod_per[d]
    a = sum(1 for k in ks if k in added)
    off = ks - added
    same = sum(1 for k in off if inn_first.get(k) == d)
    moved = len(off) - same
    moved_total += moved
    pct = a / len(ks) * 100 if ks else 0.0
    star = ' ★' if d in extra else ''
    L.append(f'| `{d}`{star} | {len(ks)} | {a} | {same} | {moved} | {pct:.1f}% |')
L.append('')
L.append('¹ 官方类在内层同名 dex 出现（就近未动） ｜ ² 官方类来自内层其他 dex（重打包挪位）')
L.append('')
for d in extra:
    ks = mod_per[d]
    a = sorted(k for k in ks if k in added)
    off = ks - set(a)
    src = Counter(inn_first.get(k, '(消失)') for k in off)
    top_add_pkgs = Counter('/'.join(k.split('/')[:2]) for k in a)
    L.append(f'### ★ 外层独有 `{d}.dex` 解剖（{len(ks)} 类）')
    L.append('')
    L.append(f'- 真新增: **{len(a)}** ｜ 官方挪入: **{len(off)}**')
    if off:
        L.append(f'- 官方来源分布（前 8）: ' + '、'.join(f'`{s}`×{c}' for s, c in src.most_common(8)))
    if a:
        L.append(f'- 新增包前缀分布（前 8）: ' + '、'.join(f'`{s}/`×{c}' for s, c in top_add_pkgs.most_common(8)))
    verdict = '纯重排放大（无新增语义）' if len(a) == 0 else ('重排为主、少量新增' if len(a) / max(1, len(ks)) < 0.1 else '新增注入堆（重点排查对象）')
    L.append(f'- 机械判读（建议，非终判）: **{verdict}**')
    L.append('')
L.append(f'- 全树官方类挪位总数（重排规模）: {moved_total}')
L.append('')

os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, 'a', encoding='utf-8') as f:
    f.write('\n'.join(L))

for d in extra:
    ks = mod_per[d]
    a = sum(1 for k in ks if k in added)
    print(f'HG3-DEX extra_dex={d} total={len(ks)} added={a} official_moved={len(ks)-a}')
print(f'HG3-DEX dex_mod={len(mod_per)} dex_inner={len(inn_per)} moved_total={moved_total}')

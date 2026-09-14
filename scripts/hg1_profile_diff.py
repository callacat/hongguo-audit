#!/usr/bin/env python3
# HG 线通用：红果壳画像 vs 番茄 round16a 已知壳类画像 → 公共类重合率
# HG-3a 参数化：HG_TAG 环境变量驱动输出文件名（默认 hg1=历史行为）。
# 输入：work/added-classes.txt（diff 脚本产出的真新增类）+ docs/profile-16a-truly-added.txt（1249 基线，可覆盖）
# 输出：{TAG}-diff-report.md 附 §7 重合率；work/overlap-classes.txt / work/hg-only-classes.txt
import os, re, sys
from collections import defaultdict

work = sys.argv[1]
TAG = os.environ.get('HG_TAG', 'hg1')
profile_file = sys.argv[2] if len(sys.argv) > 2 else 'docs/profile-16a-truly-added.txt'

def load(p):
    s = set()
    with open(p, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                s.add(line)
    return s

def norm(k):
    """画像 key 归一：去匿名类/内部类后缀 $xxx（跨版本 dex 重排时匿名类计数会漂移），统一主类名。"""
    stem = k[:-6] if k.endswith('.smali') else k
    return stem.split('$')[0]

hg = load(os.path.join(work, 'added-classes.txt'))
fp = load(profile_file)

hg_n = {norm(k) for k in hg}
fp_n = {norm(k) for k in fp}
common = hg_n & fp_n
hg_only = hg_n - fp_n

# 按包分组：重合类 & 红果独有类
def group(s):
    g = defaultdict(list)
    for k in sorted(s):
        pkg = '/'.join(k.split('/')[:-1])
        top = '/'.join(pkg.split('/')[:2]) if pkg else '(root)'
        g[top].append(k)
    return g

cg = group(common)
og = group(hg_only)

rate = len(common) / len(hg_n) * 100 if hg_n else 0.0
RED = rate < 30

out = []
out.append('')
out.append('## 7. 与番茄 round16a 壳类画像重合分析')
out.append('')
out.append(f'> 口径：主类名归一（`X$a`/`X$1` → `X`），红果真新增类 × 番茄 16a 真新增 1249 类画像。')
out.append(f'> 红果真新增 {len(hg)} 个 .smali 文件 = 归一后 **{len(hg_n)} 主类**；画像基线 {len(fp)} 归一 {len(fp_n)} 主类。')
out.append('')
out.append(f'### ★ 公共类重合率 = {len(common)} / {len(hg_n)} = **{rate:.1f}%** {"🚩 **低于 30% 红旗：作者手法疑似变化，老马需重估路线**" if RED else "（≥30%，未触红旗）"}')
out.append('')
out.append('### 重合类按包分组（A 类候选：壳代码）')
out.append('')
out.append('| 包前缀 | 类数 |')
out.append('|---|---|')
for top in sorted(cg, key=lambda x: -len(cg[x])):
    out.append(f'| `{top}/` | {len(cg[top])} |')
out.append('')
out.append('### 红果独有类按包分组（B/C/D 类候选——番茄壳中不存在）')
out.append('')
out.append('| 包前缀 | 类数 |')
out.append('|---|---|')
for top in sorted(og, key=lambda x: -len(og[x])):
    out.append(f'| `{top}/` | {len(og[top])} |')
out.append('')
out.append('### 红果独有类完整清单')
out.append('')
out.append('```')
for k in sorted(hg_only):
    out.append(k)
out.append('```')
out.append('')
out.append(f'> 画像独有（番茄有红果无，信息项）: {len(fp_n - hg_n)} 主类')
out.append('')

with open(os.path.join(work, 'diff-out', 'docs', f'{TAG}-diff-report.md'), 'a', encoding='utf-8') as f:
    f.write('\n'.join(out))

with open(os.path.join(work, 'overlap-classes.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(common)) + '\n')
with open(os.path.join(work, 'hg-only-classes.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(hg_only)) + '\n')

print(f'HG{TAG[2:] if TAG.startswith("hg") else TAG.upper()}-PROFILE total={len(hg_n)} overlap={len(common)} rate={rate:.1f}% redflag={RED} hg_only={len(hg_only)} profile_only={len(fp_n - hg_n)}')

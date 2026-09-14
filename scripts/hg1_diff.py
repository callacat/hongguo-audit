#!/usr/bin/env python3
# HG-1：红果外层 23dex vs 内嵌官方原包 21dex 全量 diff（baksmali 后按类名对齐）
# 继承番茄 round16a 两轮修正方法论：①调试指令剥离（.line/.prologue/.local/.source，保留 .catch）
# ②类名对齐排除 dex 挪位噪声（红果外层=官方 dex 重打包+patch，类必然跨 dex 挪动）
# 输入：work/smali-hg-mod/ 与 work/smali-hg-inner/（每 dex 一个子目录）
# 输出：work/diff-out/docs/hg1-diff-report.md + hg1-diff-baksmali/(added|changed|removed)/
#      work/added-classes.txt（真新增类名清单，画像重合输入）
import os, re, sys, shutil, hashlib

work = sys.argv[1]
report_path = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(work, 'diff-out', 'docs', 'hg1-diff-report.md')
MOD = os.path.join(work, 'smali-hg-mod')
INN = os.path.join(work, 'smali-hg-inner')
OUTD = os.path.dirname(report_path)
BAK = os.path.join(OUTD, 'hg1-diff-baksmali')
os.makedirs(BAK, exist_ok=True)
for s in ('added', 'changed', 'removed'):
    os.makedirs(os.path.join(BAK, s), exist_ok=True)

METHOD_RE = re.compile(r'^\.method\s+(.+)$')
DEBUG_RE = re.compile(r'^\s*\.(line|prologue|local|end local|restart local|source)\b')

def collect_by_classname(root):
    """类名(去 dex 前缀) -> (绝对路径, 来源dex列表)。同名跨 dex 冲突会记录。"""
    idx = {}
    for droot, _, fs in os.walk(root):
        for f in fs:
            if not f.endswith('.smali'):
                continue
            abs_p = os.path.join(droot, f)
            rel = os.path.relpath(abs_p, root)
            parts = rel.split(os.sep)
            dexn = parts[0] if len(parts) > 1 else 'classes'
            key = os.path.join(*parts[1:]) if len(parts) > 1 else rel
            if key in idx:
                idx[key][1].append(dexn)
            else:
                idx[key] = [abs_p, [dexn]]
    return idx

def norm_method_body(text):
    out = []
    for line in text.split('\n'):
        s = line.strip()
        if DEBUG_RE.match(line) or not s:
            continue
        out.append(s)
    return '\n'.join(out)

def parse_methods(path):
    methods, order = {}, []
    cur_name, cur_buf = None, None
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            m = METHOD_RE.match(line.strip())
            if m:
                cur_name = m.group(1).strip()
                cur_buf = [line]
            elif cur_name is not None:
                cur_buf.append(line)
                if line.strip() == '.end method':
                    body = norm_method_body(''.join(cur_buf))
                    if cur_name in methods:
                        cur_name += ' #DUP'
                    methods[cur_name] = body
                    order.append(cur_name)
                    cur_name, cur_buf = None, None
    return methods, order

mod = collect_by_classname(MOD)
inn = collect_by_classname(INN)

mod_conflict = {k: v[1] for k, v in mod.items() if len(v[1]) > 1}
inn_conflict = {k: v[1] for k, v in inn.items() if len(v[1]) > 1}

mod_keys = set(mod)
inn_keys = set(inn)
added = sorted(mod_keys - inn_keys)
removed = sorted(inn_keys - mod_keys)

method_stats = []          # (类名, a, r, c)
total_a = total_r = total_c = 0
changed_cls = []
for key in sorted(mod_keys & inn_keys):
    im, _ = parse_methods(inn[key][0])
    mm, order = parse_methods(mod[key][0])
    a = [n for n in mm if n not in im]
    r = [n for n in im if n not in mm]
    c = [n for n in mm if n in im and mm[n] != im[n]]
    if a or r or c:
        changed_cls.append(key)
        total_a += len(a); total_r += len(r); total_c += len(c)
        method_stats.append((key, len(a), len(r), len(c)))
        dst = os.path.join(BAK, 'changed', key)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w', encoding='utf-8') as out:
            out.write(f'## {key}\n# added={len(a)} removed={len(r)} changed={len(c)}\n\n')
            for n in a:
                out.write(f'.method {n}\n[MOD-ADDED]\n{mm[n]}\n\n')
            for n in c:
                out.write(f'.method {n}\n[MOD-CHANGED]\n{mm[n]}\n[INNER-ORIGINAL]\n{im[n]}\n\n')
            for n in r:
                out.write(f'.method {n}\n[INNER-REMOVED-IN-MOD]\n{im[n]}\n\n')

for key in added:
    src = mod[key][0]
    dst = os.path.join(BAK, 'added', key)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
for key in removed:
    src = inn[key][0]
    dst = os.path.join(BAK, 'removed', key)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)

with open(os.path.join(work, 'added-classes.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(added) + '\n')
with open(os.path.join(work, 'changed-classes.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(changed_cls) + '\n')

report = [f'# HG-{sys.argv[3] if len(sys.argv) > 3 else "1"} 红果外层 dex 全量 diff 报告', '',
          '> 方法=类名对齐+调试指令剥离（继承番茄 round16a 两轮修正）。分类权在老马：',
          '> A=壳代码(番茄画像重合) / B=去广告会员patch / C=可疑新增(番茄壳中不存在) / D=VIP伪造保留', '',
          '## 1. 总览', '',
          f'- 外层类总数: {len(mod_keys)} ｜ 内层官方类总数: {len(inn_keys)}',
          f'- **真新增类: {len(added)}**（全文见 hg1-diff-baksmali/added/）',
          f'- **真删除类: {len(removed)}**（全文见 hg1-diff-baksmali/removed/）',
          f'- **修改类: {len(changed_cls)}**（差异方法全文见 hg1-diff-baksmali/changed/，[MOD-ADDED]/[MOD-CHANGED vs INNER-ORIGINAL]/[INNER-REMOVED-IN-MOD] 三段标注）',
          f'- 修改类中差异方法: 新增 {total_a} / 删除 {total_r} / 修改 {total_c}', '',
          f'- 跨 dex 重复类名（mod）: {len(mod_conflict)} ｜（inner）: {len(inn_conflict)}（应为 0，非 0 需在报告红旗解释）', '',
          '## 2. 真新增类清单（按包前缀分组）', '']
groups = {}
for key in added:
    stem = key[:-6] if key.endswith('.smali') else key
    pkg = '/'.join(stem.split('/')[:-1])
    top = '/'.join(pkg.split('/')[:2]) if pkg else '(root)'
    groups.setdefault(top, []).append(key)
for top in sorted(groups, key=lambda x: -len(groups[x])):
    report.append(f'### `{top}/` — {len(groups[top])} 类')
    for k in groups[top]:
        report.append(f'- `{k}`')
    report.append('')
report += ['## 3. 修改类清单（按差异方法总数降序）', '',
           '| 类 | +新增 | -删除 | ~修改 | 合计 |', '|---|---|---|---|---|']
for key, a, r, c in sorted(method_stats, key=lambda x: -(x[1]+x[2]+x[3])):
    report.append(f'| `{key}` | {a} | {r} | {c} | {a+r+c} |')
report += ['', '## 4. 真删除类清单', '']
if removed:
    for key in removed:
        report.append(f'- `{key}`')
else:
    report.append('（无——破解者未删除任何官方类，与番茄 16a 行为一致）')
report += ['', '## 5. dex 挪位对照（重打包证据，无语义）', '',
           f'- 同名类在 mod/inner 都出现且来源 dex 不同的数量（挪位规模，信息项）: 类名对齐总数 {len(mod_keys & inn_keys)}', '',
           '## 6. 归档结构', '',
           '```', 'hg1-diff-baksmali/', '├── added/    真新增类 baksmali 全文', '├── changed/  修改类差异方法全文（三段标注）', '└── removed/  删除类 inner 全文', '```', '']
with open(report_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report))

print(f'HG1-DIFF added={len(added)} removed={len(removed)} changed={len(changed_cls)} (+{total_a}/-{total_r}/~{total_c})')
print(f'HG1-DIFF mod_cls={len(mod_keys)} inner_cls={len(inn_keys)} conflict_mod={len(mod_conflict)} conflict_inner={len(inn_conflict)}')
print(f'baksmali 归档文件数: {sum(len(fs) for _,_,fs in os.walk(BAK))}')

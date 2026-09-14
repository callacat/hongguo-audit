#!/usr/bin/env python3
# HG-3b：v7.3.7.32 C 类净化——老马终判唯一点位（勿扩面，hits≠1 直接 FAIL 阻断构建）
# 点位：smali*/com/tencent/tinker/loader/MuteApplication.smali → .method public onCreate()V 内
#       invoke-static {..}, Lcom/b/a;->init()V → 原地注释 NOP（void 返回，无寄存器语义，与 HG-2 同款保守法）
# 家族本体 com/b/a* 3 类不删不动（入口断后永不触达；防 verify missing class）。
# 输入：argv[1]=mod_src（apktool d -r 树）；argv[2]=diff 证据输出目录（可选）
# 输出：原地改写 + unified diff 落证据；stdout 机器行 HG3B_PATCH_DONE/HG3B_PATCH_FAIL
import os, re, sys, difflib

mod_src = sys.argv[1]
diff_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(mod_src.rstrip('/')), 'hg3b-point-diff')
os.makedirs(diff_dir, exist_ok=True)

INV_RE = re.compile(r'^(\s*)invoke-static\s+\{[^}]*\},\s*Lcom/b/a;->init\(\)V\s*$')
METHOD = '.method public onCreate()V'

targets = []
for d in sorted(os.listdir(mod_src)):
    p = os.path.join(mod_src, d, 'com', 'tencent', 'tinker', 'loader', 'MuteApplication.smali')
    if d.startswith('smali') and os.path.isdir(os.path.join(mod_src, d)) and os.path.isfile(p):
        targets.append(p)
if len(targets) != 1:
    print(f'HG3B_PATCH_FAIL MuteApplication 目标文件数={len(targets)}（必须恰为 1，勿扩面）')
    sys.exit(1)
p = targets[0]
orig = open(p, encoding='utf-8').read()
lines = orig.split('\n')

m_start = m_end = None
for i, ln in enumerate(lines):
    if m_start is None:
        if ln.strip() == METHOD:
            m_start = i
    elif ln.strip() == '.end method':
        m_end = i
        break
if m_start is None or m_end is None:
    print('HG3B_PATCH_FAIL 未定位 onCreate()V 方法块（点位表不符，终止）')
    sys.exit(1)

hits = 0
out = lines[:]
for i in range(m_start + 1, m_end):
    m = INV_RE.match(lines[i])
    if m:
        out[i] = (m.group(1) + '# HG3B-NOP-C: 断 C 类设备指纹链唯一外部入口 Lcom/b/a;->init()V'
                  '（v7.3.7.32 老马 HG-3b 终判单点；家族本体保留不删）')
        hits += 1
if hits != 1:
    print(f'HG3B_PATCH_FAIL onCreate 内 init invoke 命中={hits}（老马终判=1，禁止扩面/漏点）')
    sys.exit(1)

new = '\n'.join(out)
open(p, 'w', encoding='utf-8').write(new)
diffp = os.path.join(diff_dir, 'MuteApplication.onCreate.diff')
with open(diffp, 'w', encoding='utf-8') as f:
    for ln in difflib.unified_diff(orig.split('\n'), new.split('\n'),
                                   fromfile='a/' + os.path.relpath(p, mod_src),
                                   tofile='b/' + os.path.relpath(p, mod_src), lineterm=''):
        f.write(ln + '\n')
# 全树扩面哨兵：除该点位外，任何文件不得再含对 Lcom/b/a; 的 invoke（com/b 家族本体豁免）
extra = []
for d in sorted(os.listdir(mod_src)):
    sdir = os.path.join(mod_src, d)
    if not (d.startswith('smali') and os.path.isdir(sdir)):
        continue
    for droot, _, fs in os.walk(sdir):
        for f in fs:
            if not f.endswith('.smali'):
                continue
            fp = os.path.join(droot, f)
            rel = os.path.relpath(fp, mod_src)
            parts = rel.split(os.sep)
            if len(parts) >= 3 and parts[-3] == 'com' and parts[-2] == 'b':
                continue
            for j, ln in enumerate(open(fp, encoding='utf-8', errors='replace')):
                if 'Lcom/b/a;->' in ln and ln.strip().startswith('invoke-'):
                    extra.append(f'{rel}:{j+1}: {ln.strip()[:90]}')
if extra:
    print(f'HG3B_PATCH_FAIL 发现表外 invoke 点位 {len(extra)} 处（扩面红旗，终止；点位清单如下）')
    for e in extra[:20]:
        print('  ' + e)
    sys.exit(1)
print(f'HG3B_PATCH_DONE hits=1 extra_outside_table=0 file={os.path.relpath(p, mod_src)} diff={diffp}')

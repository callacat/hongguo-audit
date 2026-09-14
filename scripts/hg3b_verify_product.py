#!/usr/bin/env python3
# HG-3b：构建产物回读验证（对 signed.apk 的 baksmali 子集，子集=含 'Lcom/b/a;' 或 'MuteApplication' 字符串的 dex）
# 三道硬门：① MuteApplication.onCreate()V 编译后不再含任何 Lcom/b/a 引用且方法体仍在（NOP 落位）
#          ② com/b 之外零外部 invoke 残留（invoke 级反射入口面）
#          ③ com/b/a 家族 3 类恒等存续（mod_src 与产物路径集合对拍，防 apktool 重排误删/混入）
# 输入：argv[1]=prod_smali（产物 baksmali 子集根，每 dex 一子目录）；argv[2]=mod_src（已 patch 的 apktool 树）
# 输出：stdout 机器行 HG3B_VERIFY_*；任何门失败 exit 1
import os, re, sys

PROD = sys.argv[1]
SRC = sys.argv[2]
TARGET = 'Lcom/b/a;'
INV_RE = re.compile(r'invoke-(static|virtual|super|direct|interface)(/range)?\s+\{[^}]*\},\s*Lcom/b/a;->([\w$<>]+)\(')
METHOD = '.method public onCreate()V'

def is_family(key):
    parts = key.split(os.sep)
    return len(parts) >= 3 and parts[-3] == 'com' and parts[-2] == 'b'

def walk_strip(root):
    """产出 (path, rel, key)：key=去掉一级 dex/smali 目录前缀的类路径。"""
    for droot, _, fs in os.walk(root):
        for f in fs:
            if f.endswith('.smali'):
                p = os.path.join(droot, f)
                rel = os.path.relpath(p, root)
                parts = rel.split(os.sep)
                key = os.path.join(*parts[1:]) if len(parts) > 1 else rel
                yield p, rel, key

def walk_src(mod_src):
    for d in sorted(os.listdir(mod_src)):
        sd = os.path.join(mod_src, d)
        if not (d.startswith('smali') and os.path.isdir(sd)):
            continue
        for droot, _, fs in os.walk(sd):
            for f in fs:
                if f.endswith('.smali'):
                    p = os.path.join(droot, f)
                    yield p, os.path.relpath(p, mod_src), os.path.relpath(p, sd)

fails = []

# —— 源侧家族集合（mod_src，已 patch）——
fam_src = set(k for _, _, k in walk_src(SRC) if is_family(k))

# —— 产物侧扫描 ——
fam_prod = set()
ext_lines = []
mute = {'found': 0, 'onCreate_with_ref': 0, 'onCreate_body_lines': 0}
for p, rel, key in walk_strip(PROD):
    txt = open(p, encoding='utf-8', errors='replace').read()
    if is_family(key):
        fam_prod.add(key)
        continue
    if TARGET in txt:
        for i, ln in enumerate(txt.split('\n')):
            if INV_RE.search(ln):
                ext_lines.append(f'{rel}:{i+1}: {ln.strip()[:100]}')
    if key.endswith('MuteApplication.smali'):
        mute['found'] += 1
        in_m = False
        body = []
        for ln in txt.split('\n'):
            if not in_m and ln.strip() == METHOD:
                in_m = True
                continue
            if in_m:
                if ln.strip() == '.end method':
                    break
                body.append(ln)
        code = [l for l in body if l.strip() and not l.strip().startswith('#')]
        btxt = '\n'.join(code)  # 注释行不计（真实产物无注释；合成用例防误报，指令/伪指令级引用才算）
        mute['onCreate_body_lines'] = len(code)
        if 'Lcom/b/a' in btxt:
            mute['onCreate_with_ref'] += 1
            fails.append(f'门①失败: {rel} onCreate()V 仍含 Lcom/b/a 引用（NOP 未落位到编译产物）')

if mute['found'] != 1:
    fails.append(f"门①失败: 产物子集中 MuteApplication.smali 数={mute['found']}（必须恰为 1，子集 dex 选择或重排异常）")
elif mute['onCreate_body_lines'] < 3:
    fails.append(f"门①失败: MuteApplication.onCreate 方法体有效指令行仅 {mute['onCreate_body_lines']}（疑似被过度改写）")

if ext_lines:
    fails.append(f'门②失败: com/b 之外外部 invoke 残留 {len(ext_lines)} 处')
    for e in ext_lines[:20]:
        print('  EXT ' + e)

if fam_prod != fam_src:
    only_src = sorted(fam_src - fam_prod)
    only_prod = sorted(fam_prod - fam_src)
    fails.append(f'门③失败: 家族集合不一致 src={len(fam_src)} prod={len(fam_prod)} 源独有={only_src} 产物独有={only_prod}')
elif len(fam_prod) != 3:
    fails.append(f'门③失败: 家族类数={len(fam_prod)} ≠3（与 v736/v737 审计基线不符）')

for k in sorted(fam_prod):
    print(f'HG3B_VERIFY_FAMILY {k}')
print(f"HG3B_VERIFY mute_found={mute['found']} mute_oncreate_ref={mute['onCreate_with_ref']} "
      f"mute_oncreate_body={mute['onCreate_body_lines']} ext_invoke={len(ext_lines)} "
      f"family_src={len(fam_src)} family_prod={len(fam_prod)}")
if fails:
    for f in fails:
        print('HG3B_VERIFY_FAIL ' + f)
    sys.exit(1)
print('HG3B_VERIFY_OK gates=[mute_nop_landed=1, ext_invoke=0, family_identity=3/3]')

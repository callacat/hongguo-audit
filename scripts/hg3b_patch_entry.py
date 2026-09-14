#!/usr/bin/env python3
from pathlib import Path
import difflib
import sys

mod_src = Path(sys.argv[1])
diff_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else mod_src.parent / 'hg3b-point-diff'
entry = mod_src / 'smali_classes4/com/tencent/tinker/loader/MuteApplication.smali'
target = 'invoke-static {}, Lcom/b/a;->init()V'

if not entry.is_file():
    raise SystemExit(f'entry not found: {entry}')

original = entry.read_text(encoding='utf-8', errors='replace')
lines = original.splitlines()
hits = []
for index, line in enumerate(lines):
    if line.strip() == target:
        indent = line[:len(line) - len(line.lstrip())]
        lines[index] = f'{indent}# HG3B-NOP-C: 断 invoke-static {{}} Lcom/b/a;->init()V（C 类设备指纹链入口）'
        hits.append(index + 1)
        break

if len(hits) != 1:
    raise SystemExit(f'expected exactly one target invocation, found {len(hits)}')

patched = '\n'.join(lines) + ('\n' if original.endswith('\n') else '')
diff_dir.mkdir(parents=True, exist_ok=True)
diff_path = diff_dir / 'MuteApplication.diff'
diff_path.write_text('\n'.join(difflib.unified_diff(
    original.splitlines(), patched.splitlines(), fromfile=f'a/{entry.relative_to(mod_src)}', tofile=f'b/{entry.relative_to(mod_src)}', lineterm='')) + '\n', encoding='utf-8')
entry.write_text(patched, encoding='utf-8')
print(f'HG3B_DIFF {entry.relative_to(mod_src)} -> {diff_path}')
print(f'HG3B_PATCH_DONE files=1 invokes=1 lines={hits}')

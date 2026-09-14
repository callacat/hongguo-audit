#!/usr/bin/env python3
# HG-3: mechanical rescan of the com/b/a family and its external references.
import os
import re
import sys
from collections import defaultdict

work = sys.argv[1]
report_path = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(work, 'diff-out', 'docs', 'hg3-cba-scan.md')
smali_root = os.path.join(work, 'smali-hg-mod')

FAMILY_PREFIX = 'com/b/a'
INVOCATION_RE = re.compile(r'invoke-[a-z]+.*Lcom/b/a;->[^\s,]+')
FIELD_RE = re.compile(r'[si]-?(?:get|put)-[^\s]+.*Lcom/b/a;->[^\s,]+')

def is_family_file(relative_key):
    return relative_key == f'{FAMILY_PREFIX}.smali' or relative_key.startswith(f'{FAMILY_PREFIX}$')

family = defaultdict(list)
external = defaultdict(list)

for directory, _, files in os.walk(smali_root):
    for filename in files:
        if not filename.endswith('.smali'):
            continue
        path = os.path.join(directory, filename)
        relative_key = os.path.relpath(path, smali_root).replace(os.sep, '/')
        with open(path, encoding='utf-8', errors='replace') as handle:
            for line_number, line in enumerate(handle, 1):
                if 'Lcom/b/a;->' not in line:
                    continue
                if INVOCATION_RE.search(line) or FIELD_RE.search(line):
                    if is_family_file(relative_key):
                        family[relative_key].append((line_number, line.strip()))
                    else:
                        external[relative_key].append((line_number, line.strip()))

lines = [
    '# HG-3 com/b/a family rescan',
    '',
    f'- Source: `smali-hg-mod` baksmali output.',
    f'- Family files: {len(family)}',
    f'- Family reference lines: {sum(len(values) for values in family.values())}',
    f'- External referencing files: {len(external)}',
    f'- External reference lines: {sum(len(values) for values in external.values())}',
    '',
    '## Family files',
    '',
]

for key in sorted(family):
    lines.append(f'### `{key}`')
    lines.append('')
    lines.append('| line | reference |')
    lines.append('|---:|---|')
    for line_number, text in family[key]:
        lines.append(f'| {line_number} | `{text}` |')
    lines.append('')

lines += ['## External reference points', '']
if external:
    for key in sorted(external):
        lines.append(f'### `{key}`')
        lines.append('')
        lines.append('| line | reference |')
        lines.append('|---:|---|')
        for line_number, text in external[key]:
            lines.append(f'| {line_number} | `{text}` |')
        lines.append('')
else:
    lines.append('(none)')

os.makedirs(os.path.dirname(report_path), exist_ok=True)
with open(report_path, 'w', encoding='utf-8') as handle:
    handle.write('\n'.join(lines))

print(f'HG3-CBA family_files={len(family)} family_refs={sum(len(v) for v in family.values())} external_files={len(external)} external_refs={sum(len(v) for v in external.values())}')

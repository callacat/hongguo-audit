#!/usr/bin/env python3
# HG-2：C 类后门 com/b/a 设备指纹链清除——全树「外部 invoke-NOP」（掐入口不撒网，学番茄 16b/17b）
# 原则（老马终判）：不整删 com/b/a 家族类（防引用完整性/verify 崩），只断外部对它的 invoke；
#   com/b/ 包内自引用豁免（init→getApplication→Android_id→getReflect 是链内部，保留无害，入口一断永不执行）。
# 输入：mod_src（apktool d 解出目录，含 smali*/）
# 输出：原地改写 .smali + stdout 命中明细（供 hg2 报告回填，断言外部命中数=2）
import os, re, sys, difflib

mod_src = sys.argv[1]
diff_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(mod_src.rstrip('/')), 'hg2-point-diff')
os.makedirs(diff_dir, exist_ok=True)
TARGET = 'Lcom/b/a;'

INVOKE_RE = re.compile(r'^(\s*)invoke-([a-z]+)\s+\{([^}]*)\},\s*' + re.escape(TARGET) + r'->([\w$<>]+)\(([^)]*)\)(\S+)\s*$')
RET_RE = re.compile(r'^(\s*)move-result(-object|-wide)?\s+(v\d+|p\d+)\s*$')

def ret_kind(desc_ret):
    return desc_ret  # V / Ljava/lang/String; / I / J / ...

def patch_file(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    out, hits = [], 0
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m = INVOKE_RE.match(line)
        if m:
            indent, _, _, name, args, ret = m.groups()
            # void 调用：整条 invoke 删除（NOP）
            if ret == 'V':
                out.append(f'{indent}# HG2-NOP-C: 断 invoke-static {{}} L{TARGET[1:-1]};->{name}()V（C 类设备指纹链入口）')
                hits += 1
                i += 1
                continue
            # 非 void：删 invoke，向后同方法内配对第一条 move-result → 换安全兜底 const
            #   先输出注释占位，再在后续行处理 move-result
            out.append(f'{indent}# HG2-NOP-C: 断 invoke-... L{TARGET[1:-1]};->{name}({args}){ret}（C 类·返回值兜底见下）')
            hits += 1
            i += 1
            # 向后扫（跳过空行）找 move-result 配对；遇 .end method / 下一 .method 则视为无消费
            replaced = False
            while i < n:
                nxt = lines[i]
                rr = RET_RE.match(nxt)
                if rr:
                    rindent, rkind, rreg = rr.groups()
                    rkind = rkind or ''
                    if rkind == '-object':
                        if ret.startswith('Ljava/lang/String;') or 'String' in ret:
                            repl = f'{rindent}const-string {rreg}, ""'
                        else:
                            repl = f'{rindent}const/4 {rreg}, 0x0  # HG2-C: 非 String 对象返回值置 null'
                    elif rkind == '-wide':
                        repl = f'{rindent}const-wide/16 {rreg}, 0x0'
                    else:  # move-result (int/short/...)
                        repl = f'{rindent}const/4 {rreg}, 0x0'
                    out.append(f'{repl}  # HG2-NOP-C: 原 L{TARGET[1:-1]};->{name} 返回值兜底')
                    replaced = True
                    i += 1
                    break
                if nxt.strip().startswith('.end method') or nxt.strip().startswith('.method'):
                    break
                out.append(nxt)
                i += 1
            if not replaced:
                out.append(f'{indent}# HG2-NOP-C-WARN: invoke {name} 返回值非 void 但未配对到 move-result（无消费/异常结构），已仅断 invoke')
            continue
        out.append(line)
        i += 1
    return '\n'.join(out), hits

def is_internal(path, root):
    # 类体自引用豁免：文件位于 smali*/com/b/... 下的 com/b/a 家族本体
    rel = os.path.relpath(path, root)
    parts = rel.split(os.sep)
    # parts = [smali*, com, b, a....smali]
    return len(parts) >= 3 and parts[-3] == 'com' and parts[-2] == 'b'

external_hits = {}
internal_skipped = 0
for d in sorted(os.listdir(mod_src)):
    sdir = os.path.join(mod_src, d)
    if not (d.startswith('smali') and os.path.isdir(sdir)):
        continue
    for droot, _, fs in os.walk(sdir):
        for f in fs:
            if not f.endswith('.smali'):
                continue
            p = os.path.join(droot, f)
            txt = open(p, encoding='utf-8', errors='replace').read()
            if TARGET not in txt:
                continue
            if is_internal(p, mod_src):
                internal_skipped += 1
                continue
            newtxt, hits = patch_file(p)
            if hits:
                rel = os.path.relpath(p, mod_src)
                external_hits[rel] = hits
                # 逐点位 diff 证据：原文件临时备份 → unified diff 落 diff_dir
                orig = '\n'.join(open(p, encoding='utf-8', errors='replace').read().split('\n'))
                diffp = os.path.join(diff_dir, rel.replace(os.sep, '__') + '.diff')
                with open(diffp, 'w', encoding='utf-8') as df:
                    for ln in difflib.unified_diff(orig.split('\n'), newtxt.split('\n'),
                                                   fromfile='a/' + rel, tofile='b/' + rel, lineterm=''):
                        df.write(ln + '\n')
                print(f'HG2_DIFF {rel} -> {diffp}')
                open(p, 'w', encoding='utf-8').write(newtxt)

print(f'HG2_PATCH_DONE external_files={len(external_hits)} total_invokes={sum(external_hits.values())} internal_skipped={internal_skipped}')
for rel, h in sorted(external_hits.items()):
    print(f'HG2_HIT {h}  {rel}')
if sum(external_hits.values()) != 2:
    print(f'HG2_COUNT_WARN 外部 invoke 命中={sum(external_hits.values())}（老马终判=2，偏差需人工核，不阻断但报告标红）')

# hongguo-audit

红果免费短剧破解底包安全审计 + 净化构建工作区（HG 线，2026-09-15 已终态含 HG-3）。纯分析/构建仓：不含任何 APK（样本与产物全部走 Release），仓内只有脚本与报告。

## 任务线终态（2026-09-15 更新）
| 轮次 | 内容 | CI | 产物 |
|---|---|---|---|
| HG-1 | v7.3.6.32 会员版外层壳后门审计（三方 dex diff + 端点提取） | run 34697350594 ✅ | docs/hg1-* + Release hg1-artifacts |
| HG-2 | 净化重打包：除 C 类后门 com/b/a 设备指纹链，保 A壳/B去广告/D会员 | run 34703840399 ✅ | Release **hg2-round1**（clean-r1.apk, sha256 6ae5ab68…723123） |
| HG-3a | v7.3.7.32 新底包审计（**CC×Codex 双引擎对照实验**，东哥 9-14 拍板） | CC run 34875020820 ✅一发过 ｜ Codex run 34888317725 ✅第4次 | docs/hg3-diff-report-cc.md(5021行) + hg3-endpoints-cc.md + INDEX；Codex 线 docs/hg3-diff-report-codex.md（分支 hg3-codex）；归档 Release hg3-artifacts-cc |
| HG-3b | v7.3.7.32 净化构建（同点位单点 NOP：MuteApplication.onCreate→com.b.a.init） | CC run 34894618801 ✅ ｜ Codex run 34900712742 ✅(r5) | Release **hg3b-round1-cc**（选定交付，sha256 598d6d28…939f）＋ Release hg3b-codex-r5（对照产物） |

**v7.3.7.32 真机实测**：东哥手机 2026-09-15 覆盖安装通过（与 HG-2 同 codery keystore，`install -r` 零数据损失）。判据链：内层 base.apk sha256=a49cf486…bf9 字节级不变、com/b 外部 invoke=0、家族 3 类保留静默、v1v2v3 全签。
**对照实验结论（9-15）**：CC 胜（效率 1h15min vs 3.5h、CI 1 次 vs 4 次、classes24 归属判定 CC 正确/Codex 有自相矛盾 bug）；Codex 增值=HG-1 增量对比维度（new 93/missing 134）；六判据五对一拍全咬合（老马独立基线互印）。Codex 适合窄指令+短任务书，宽任务书长会话易漂移——台账见老马侧 .tasks/codery-team-ops。

## 关键结论（HG-1/HG-3a 老马终判）
- 与番茄破解版**同一作者**（外层签名证书 SHA-256 逐字节一致 eae34eaf…c328）、同一手法（assets 内嵌官方原包+外层打 patch）；v7.3.7.32 依旧同作者换版本（壳画像重合 92.4%，v736→v737 增量+4 类，结构同构）
- v7.3.7.32：真新增 1228 类 / 删除 0 / 改 3527；壳端点 URL=0 IP=0 无 C2；classes23/24=壳 dex（classes24 新增占比 55.8%=会员/去广告注入堆）；`hg1/hg3 端点清单` §3 "🚩大漂移"为基线口径误报（已归案，勿再引用）
- C 类后门唯一发现：`com/b/a`（ActivityThread 反射 + deviceid 生成 + ANDROID_ID 篡改），外部入口= MuteApplication.onCreate 1 处（HG-1 终判"调用方2"系含家族内部自调，勘误已录）；净化=单点 NOP（保守法，家族本体保留静默）

## 样本（Release `samples`，勿入 git）
| asset | sha256 | 说明 |
|---|---|---|
| hongguo-v7.3.6.32-crack.apk | 1c2c0bb4…b751cd | 破解底包 v23dex（workflow 内 mv 为 member 名对齐历史引用） |
| hongguo-73632-inner-official.apk | 8f062c16…dcfd | 内嵌官方原包 7.3.6.32（v1v2 签名完整） |
| hongguo-v7.3.7.32-crack.apk | 337ff941…4b16e | 破解底包 v24dex（HG-3 线） |
| hongguo-73732-inner-official.apk | a49cf486…955bf9 | 内嵌官方原包 7.3.7.32 |

## 脚本与 CI
- `scripts/hg1_diff.py` / `hg1_profile_diff.py` / `hg1_endpoints.py` — 审计三件套，HG-3a 起支持 `HG_TAG`/`HG_VER` 环境变量参数化（默认值=HG-1 历史行为，旧 workflow 零改动可复跑）
- `scripts/hg3_dex_attribution.py` / `hg3_scan_c.py` — 逐 dex 归属解剖（重排 vs 注入堆）+ C 家族存续复扫（HG-3a，CC 线）
- `scripts/hg3b_patch_c.py` / `hg3b_verify_product.py` — 净化单点 NOP + 产物回读三门（HG-3b，CC 线）
- workflow：`hongguo-crack-audit.yml`/`hongguo-crack-clean-build.yml`（v736 冻结线）；`hongguo-crack-audit-param.yml`/`hongguo-crack-clean-build-param.yml`（参数化 v737 线，默认输入=7.3.7.32，后续版本改输入即复刻）
- Secrets：KEYSTORE_BASE64/PASSWORD/ALIAS/KEY_PASSWORD（codery keystore，与番茄 v9 同源，老马 9-12 配置）
- Codex 对照线（hg3-codex 分支）：scripts/hg3_cba_scan.py、hg3b_patch_entry.py 及其 workflow 保留在分支作档案，不并 main（避免同点位双实现）
- 红果官方后续版本更新：重传新底包→param 两 workflow 顺序 dispatch 即复刻全流程

## 归档再生
baksmali 差异全文在 Release `hg1-artifacts`（不进 git）；`docs/hg1-diff-baksmali-INDEX.md` 为索引。

仅供本地个人研究，不分发。

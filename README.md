# hongguo-audit

红果免费短剧破解底包安全审计 + 净化构建工作区（HG 线，rid recvuZTO9AeaYr，2026-09-13 已终态）。纯分析/构建仓：不含任何 APK（样本与产物全部走 Release），仓内只有脚本与报告。

## 任务线终态（2026-09-13）
| 轮次 | 内容 | CI | 产物 |
|---|---|---|---|
| HG-1 | v7.3.6.32 会员版外层壳后门审计（三方 dex diff + 端点提取） | run 34697350594 ✅ | docs/hg1-* + Release hg1-artifacts |
| HG-2 | 净化重打包：除 C 类后门 com/b/a 设备指纹链，保 A壳/B去广告/D会员 | run 34703840399 ✅ | Release **hg2-round1**（clean-r1.apk, sha256 6ae5ab68…723123） |

**真机实测**：PJD110 四判据全过（装机 7.3.6.32 / 冷启动 170s 稳定无 FATAL / 无版本拦截 / 短剧真实播放无广告）+ 东哥手机复测正常。产物判据：内层 assets/base.apk sha256=8f062c16…dcfd 字节级不变、v1v2v3 全签（codery keystore，作者 CN=L 私钥不可得→覆盖装作者原版需先卸载）。

## 关键结论（HG-1 老马终判）
- 与番茄破解版**同一作者**（外层签名证书 SHA-256 逐字节一致 eae34eaf…c328）、同一手法（assets 内嵌官方原包+外层打 patch）；壳画像重合率 92.6%（1123/1213 主类）
- 真新增 1223 类 / 删除 0；壳端点 URL=0 IP=0 无 C2；`hg1-端点清单.md` §3 "🚩大漂移"为基线口径误报（已归案，勿再引用）
- C 类后门唯一发现：`com/b/a`（ActivityThread 反射 + deviceid 生成 + ANDROID_ID 篡改），外部入口= MuteApplication.onCreate 1 处（HG-1 终判"调用方2"系含家族内部自调，勘误已录）

## 样本（Release `samples`，勿入 git）
| asset | sha256 | 说明 |
|---|---|---|
| hongguo-v7.3.6.32-crack.apk | 1c2c0bb4…b751cd | 破解底包（238MB，workflow 内 mv 为 member 名对齐历史引用） |
| hongguo-73632-inner-official.apk | 8f062c16…dcfd | 内嵌官方原包（v1v2 签名完整） |

## 脚本与 CI
- `scripts/hg1_diff.py` / `hg1_profile_diff.py` / `hg1_endpoints.py` — HG-1 审计三件套（workflow: hongguo-crack-audit.yml）
- `scripts/hg2_patch_c.py` — C 链 invoke-NOP + 返回值兜底 + 双完整性门（workflow: hongguo-crack-clean-build.yml）
- Secrets：KEYSTORE_BASE64/PASSWORD/ALIAS/KEY_PASSWORD（codery keystore，与番茄 v9 同源，老马 9-12 配置）
- 红果官方后续版本更新：重传新底包→两条 workflow 顺序 dispatch 即复刻全流程

## 归档再生
baksmali 差异全文在 Release `hg1-artifacts`（不进 git）；`docs/hg1-diff-baksmali-INDEX.md` 为索引。

仅供本地个人研究，不分发。

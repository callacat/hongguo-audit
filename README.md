# hongguo-audit

红果免费短剧破解底包安全审计工作区（HG 线）。纯分析仓：不含任何 APK（样本走 Release `samples`，产物归档走 Release `hg1-artifacts`），仓内只有审计脚本与报告。

## 任务线
- **HG-1**（rid recvuZTO9AeaYr）：v7.3.6.32 会员版外层壳后门审计 = 反编译三方 diff + 端点提取。CI：`.github/workflows/hongguo-crack-audit.yml`（workflow_dispatch）。
- 方法论继承自番茄 round16a（fanqie-builder 仓，同作者：外层签名证书 SHA-256 逐字节一致）。

## 样本（Release `samples`，勿入 git）
| 文件 | sha256 | 说明 |
|---|---|---|
| hongguo-v7.3.6.32-member.apk | 1c2c0bb4…751cd | 破解底包（外层 23dex，assets/base.apk 内嵌官方） |
| hongguo-73632-inner-official.apk | 8f062c16…dcfd | 已抽出内嵌官方原包（v1v2 签名完整） |

## 脚本
- `scripts/hg1_diff.py` — 外层 vs 内层官方全量 dex diff（类名对齐+调试指令剥离）
- `scripts/hg1_profile_diff.py` — 红果壳画像 vs 番茄 16a（docs/profile-16a-truly-added.txt）重合率
- `scripts/hg1_endpoints.py` — 硬编码端点提取 + 番茄壳端点漂移比对

仅供本地个人研究，不分发。

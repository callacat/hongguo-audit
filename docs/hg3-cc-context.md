# HG-3a 审计轮 · cc 引擎上下文留痕（跨会话续命文件）

> 任务：v7.3.6.32 → v7.3.7.32 底包升级审计。引擎标识=cc，分支=hg3-cc。判定权在老马。
> 本文件由码农（Claude Code 引擎）维护，每完成一步即更新；被回收后任何续跑者从「当前状态」接续。

## 当前状态（2026-09-15 更新）
- [x] 现状盘点：HG-1 workflow/三脚本读毕；基线数字取齐（见下）
- [x] 脚本参数化：hg1_diff/hg1_profile_diff/hg1_endpoints 改 HG_TAG/HG_VER env 驱动，默认值保持 HG-1 行为；构造样例双模式回归通过（commit 4e60886）
- [x] 新脚本：scripts/hg3_scan_c.py（C 家族存续复扫，只读）+ scripts/hg3_dex_attribution.py（dex 归属解剖）（commit a24e994）
- [ ] workflow 参数化：.github/workflows/hongguo-crack-audit-param.yml 新写（输入版本/资产/sha/tag/engine；外层 unzip -o；回写 dispatch 分支；Release hg3-artifacts-cc）
- [ ] push origin hg3-cc + dispatch
- [ ] CI 跑通（可能需 1-2 轮修错重触发）
- [ ] 下载归档核验 + 组装 docs/hg3-diff-report-cc.md
- [ ] 汇报（表格/群/A2A 三选一）

## 路线决策（对 HG-1 线破坏最小原则）
1. **不改** hongguo-crack-audit.yml：它 checkout main/推 main/写 docs/hg1-*，动它=动已收官线。复制为 -param.yml，HG-1 线冻结。
2. 文件名不锁版本号（-v737）而用 -param + inputs 默认 v7.3.7.32：后续 v7.3.8.x 直接改输入复跑。
3. 回写目标=dispatch 分支（github.ref_name），永不触 main。
4. docs/Release 产物带 `-$ENGINE` 后缀：与 Codex 对照线（hg3-codex）共享仓但互不碰撞。
5. 三件套脚本 env 参数化而非新写副本：单源维护，默认值=历史行为，旧线可复现性不破。

## HG-1/v736 基线数字（增量对比用，抄自 docs/ 与 README）
- 外层类 283855 ｜ 内层 282632 ｜ 真新增 1223（归一 1213 主类）｜ 真删除 0 ｜ 修改类 3539（+14021/-30/~9921 方法）
- 画像重合 1123/1213 = 92.6%（基线 profile-16a 1249 归一 1213）
- 端点：壳 URL=0 IP=0 域名=27；漂移 dom=12（§3"大漂移"系基线口径误报，已归案勿再引用）
- C 家族 v736：3 类（com/b/a、a$Android_id、a$Reflect）；外部 invoke=1 点位（MuteApplication.onCreate→init()V）；家族自引用文件=2；内层官方包引用=0
- dex：v736 外层 23 vs 内层 21；v737 外层 24（重点：classes24.dex 归属）

## 新底包（Release samples，老马初检已实锤，勿重复 sha 初检）
- hongguo-v7.3.7.32-crack.apk 238,198,144B sha256=337ff9417e672eb407ffd42481bd58eb33bea43ddd5762e1217f07597254b16e
- hongguo-73732-inner-official.apk 134,334,100B sha256=a49cf486fb6c96d7b9169b3fa6a4a020295a8e46b78949b6b30fadc29b955bf9（CN=novel v1+v2=官方原包）

## 环境备忘（本机会话）
- gh/git 走代理：`HTTPS_PROXY=http://192.168.1.150:30001`（gh）；repo 已配 http.proxy（git）
- token 有效（gh api user=callacat）；D7 铁律：本机禁 apktool/baksmali/大 dex，重活全 CI
- dispatch 命令模板：
  `HTTPS_PROXY=... gh workflow run hongguo-crack-audit-param.yml --ref hg3-cc -R callacat/hongguo-audit`（inputs 走默认值即 v737 双样本+tag=hg3+engine=cc）
- 看 run：`gh run list/ watch/view --log-failed`

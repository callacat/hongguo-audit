# HG-2 净化蓝图（C 类后门 com/b/a 设备指纹链清除）

任务 rid recvuZTO9AeaYr ｜ 分类权威=老马 HG-1 终判（重合率 92.6%，1123/1213 主类）｜ 执行：码农（全 CI）
CI：`.github/workflows/hongguo-crack-clean-build.yml`（workflow_dispatch，`scripts/hg2_patch_c.py`）

## 0. 策略总纲
- **只断 Java 外部 invoke，不整删类**（番茄 16b/17b 教训：整删家族类引发引用完整性/verify 崩链；掐入口即全链静默）。
- com/b/a 家族 3 类（`a` + `a$Android_id` + `a$Reflect`）**保留在包内**（老马终判"不整删"；断链后永不执行，且防 verify 报 missing class）。
- A 壳（pandora/tinker/lsposed/pine/sgcore0 等 1123 重合主类）、B 去广告 patch、D 会员徽章——**零改动**。so / 内层 base.apk——**零改动**（构建双门核验）。

## 1. C 链静态画像（HG-1 归档实锤）
| 组件 | 行为 | 证据 |
|---|---|---|
| `Lcom/b/a;->init()V` | 生成/复用随机 16hex 设备 ID，写 SharedPrefs `Device`{deviceid,time,init}，再调 Android_id | hg1-diff-baksmali/added/com/b/a.smali |
| `Lcom/b/a;->getApplication()` | ActivityThread 反射取 Application（clinit 即执行一次） | 同上 |
| `Lcom/b/a$Android_id` | InvocationHandler 反射改 `Settings$Secure.sNameValueCache`（ANDROID_ID 篡改） | added/com/b/a$Android_id.smali |
| `Lcom/b/a;->getID()/getReflect()` | getter（调用方候选） | a.smali |

## 2. 断链点位表（全树自适应；invoke 级，非行号级）
> 定位法：baksmali/apktool 全树 grep `Lcom/b/a;->`，`smali*/com/b/` 本体豁免（内部自链保留），其余=外部点位逐条 NOP。
> 命中数硬校验：老马终判=2 个调用方。≠2 → log 告警 `HG2_COUNT_WARN`，人工归案（多=老马口径外新调用方；少=调用形态非标准 invoke）。

| # | 点位 | 现状 | 改法 | 状态 |
|---|---|---|---|---|
| C-1 | `com/tencent/tinker/loader/MuteApplication.smali` → `onCreate()` 首行 | `invoke-static {}, Lcom/b/a;->init()V` | 删 invoke（void 直接 NOP；壳入口方法后续逻辑不动） | 归档实锤 |
| C-2 | 待 CI 全树枚举回填（`patch-hg2.log` HG2_HIT 行） | 疑 `getID()Ljava/lang/String;` 类读取点 | 非 void → NOP invoke + move-result 换 const 兜底（String→`""`，对象→null，宽→0L，整→0） | ⏳ CI 回填 |

## 3. 构建配方（全 CI，D7）
apktool `d -f -r`（保资源不重编）→ `hg2_patch_c.py` → 自检硬门 → apktool `b -f` → `zipalign -f -p 16` → `apksigner v1+v2+v3`（codery keystore）→ 完整性后门 → Release `hg2-roundN`（N 自增）。

## 4. 完整性硬门（构建期 assert）
- ① 解包即验：`apktool` 解出的 `assets/base.apk` sha256 == 内层登记值 `8f062c16…dcfd`（样本未损坏）
- ② 产物内验：重签包内 `assets/base.apk` sha256 同上不变 + 外层 dex 数=23 + 外部 `Lcom/b/a;->` 活引用=0 + 家族 3 类俱在

## 5. 签名证书说明（⚠ 与任务书差异，主动向老马报备）
任务书要求"沿用现用 CN=L keystore 保同证书覆盖安装"。**作者 CN=L 私钥不可得**（破解者不会外流；我们仅有其证书 SHA256 `eae34…`）。番茄线先例（v9）即改用 codery 自签 keystore，实测老马可装（全新安装路径）。本构建沿用**同一把 codery keystore**（`keystore-first-run`，与 v9 同源）→ 与未来红果 HG-x 净化版互覆盖无障碍；**覆盖装作者原版底包需先卸载**（Signature mismatch，Android 硬约束，非缺陷）。若老马坚持要 CN=L 私钥路径=向作者侧要（超出码农能力）。

## 6. 风险与降级
- apktool 重编 23 dex（219MB）资源面：aapt2 拒收点按番茄五跑实锤预清（public.xml invalid*/res/invalid*）；若仍有新拒收→按点位表补预清后重跑（round 自增不冲突）。
- 若 b 步骤 dex 合并异常（作者包 dex 分布特殊）：降级配方=只替换被改的 dex（baksmali→smali 单 dex 汇编→zip 原位替换 classesN.dex + zipalign 重签），内层零风险。此降级仅在 round1 失败时启用。

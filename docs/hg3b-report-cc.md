# HG-3b 净化构建报告（v7.3.7.32，引擎=cc）

- **任务**：C 类单点净化（老马 HG-3a 终判唯一点位）+ CI 重打包签名。**判定权在老马，本轮零扩面。**
- **结论**：✅ 构建成功，三道完整性硬门全过，产物已发 Release `hg3b-round1-cc`。
- **CI run**：[#2 / 34894618801](https://github.com/callacat/hongguo-audit/actions/runs/34894618801)（hg3-cc 分支，push 自触发，`conclusion=success`）
- **产物**：`hongguo-v7.3.7.32-clean-r1-cc.apk` ｜ size=**277,643,531 B** ｜ sha256=**`598d6d28ffe866f9b5acbfa227119e0e5d767e0295cae6537b8db295ed98939f`**（CI 计算，本机下载后复算一致）
- **样本基线**：外层 `hongguo-v7.3.7.32-crack.apk`（sha=337ff941…b16e）；内层官方基准 sha=`a49cf486fb6c96d7b9169b3fa6a4a020295a8e46b78949b6b30fadc29b955bf9`

## 1. 净化点位 diff（唯一一处，全仓其余 0 改动）

`smali_classes14/com/tencent/tinker/loader/MuteApplication.smali` → `.method public onCreate()V`（全文见 `docs/hg3b-point-diff-cc.diff`）：

```diff
@@ -1126,7 +1126,7 @@
 .method public onCreate()V
     .locals 6
 
-    invoke-static {}, Lcom/b/a;->init()V
+    # HG3B-NOP-C: 断 C 类设备指纹链唯一外部入口 Lcom/b/a;->init()V（v7.3.7.32 老马 HG-3b 终判单点；家族本体保留不删）
 
     const-string v0, "Mute.App"
```

- 改法=HG-2 同款保守法：void 返回 invoke 原地注释，寄存器语义零影响。
- patch 脚本 `scripts/hg3b_patch_c.py` 机器行（CI 实录，`docs/hg3b-patch-cc.log`）：
  `HG3B_PATCH_DONE hits=1 extra_outside_table=0 file=smali_classes14/com/tencent/tinker/loader/MuteApplication.smali`
  ——命中恰 1、表外点位 0（strict：hits≠1 即中断构建）。

## 2. 保留面（按任务表，一律未动）

| 面 | 处置 |
|---|---|
| A 壳 1125 类 | 全保留 |
| B 去广告会员 patch 3527 改类 | 全保留 |
| C 家族本体 `com/b/a` `a$Android_id` `a$Reflect` 3 类 | **不删不动**（入口断后永不触达；防 verify missing class） |
| D 业务新增（含 classes24 dragon 系 1172 注入类=会员引擎面） | 全保留 |
| 内层 `assets/base.apk` | 字节级不动（双门实锤见 §3） |

## 3. 完整性硬门输出（CI 实录 + 本机独立复核）

**门①（解包侧，20:44:34Z）**：外层解出 `smali 树: 290644 文件 ｜ dex 目录: 24`；
`sha256sum mod_src/assets/base.apk` → `a49cf486fb6c96d7b9169b3fa6a4a020295a8e46b78949b6b30fadc29b955bf9` == 内层官方包 ✅

**门②（产物侧）**：`产物内层 base.apk sha256: a49cf486…` ＋ `dex 数: 24` → `HG3B_INTEGRITY_PASS` ✅

**门③（产物 smali 回读三门）**：产物 dex 按后门相关字符串选子集（回读子集 dex 数=3）baksmali 逐点位回读（`scripts/hg3b_verify_product.py`，`docs/hg3b-verify-readback-cc.log`）：

```
HG3B_VERIFY_FAMILY com/b/a$Android_id.smali
HG3B_VERIFY_FAMILY com/b/a$Reflect.smali
HG3B_VERIFY_FAMILY com/b/a.smali
HG3B_VERIFY mute_found=1 mute_oncreate_ref=0 mute_oncreate_body=42 ext_invoke=0 family_src=3 family_prod=3
HG3B_VERIFY_OK gates=[mute_nop_landed=1, ext_invoke=0, family_identity=3/3]
```

——①NOP 已落位到编译产物（onCreate 42 条有效指令完整、零 Lcom/b/a 引用）②com/b 外零外部 invoke 残留 ③家族 3 类与源树恒等 ✅

**本机独立复核（仅 curl+sha256，D7 约束）**：产物下载后 `sha256sum -c` CI 记录 = **OK**；python 直读产物 `assets/base.apk` 复算 = `a49cf486fb6c96d7b9169b3fa6a4a020295a8e46b78949b6b30fadc29b955bf9` **INNER_MATCH**，dex 数 24。

## 4. apksigner verify 全文（CI 内完成，`docs/hg3b-verify-cc.txt`）

```
Verifies
Verified using v1 scheme (JAR signing): true
Verified using v2 scheme (APK Signature Scheme v2): true
Verified using v3 scheme (APK Signature Scheme v3): true
Verified using v3.1 scheme (APK Signature Scheme v3.1): false
Verified using v4 scheme (APK Signature Scheme v4): false
Verified for SourceStamp: false
Number of signers: 1
Signer #1 certificate DN: CN=Codery Debug, O=Codery, C=CN
Signer #1 certificate SHA-256 digest: bebb2cca93e02771751af4050a72a8a37986c3c052632a8aa715421d89ffc061
Signer #1 certificate SHA-1 digest: 6fcc22082800d12db59af1c2ba1be17ed4ceef88
Signer #1 certificate MD5 digest: 27920b5a97c79693362baf1de9150557
Signer #1 key algorithm: RSA
Signer #1 key size (bits): 2048
Signer #1 public key SHA-256 digest: 1881a09a082ca5f0be96d58c42bf051ae800f0e546a510948f911ea860f30d35
Signer #1 public key SHA-1 digest: 8a4b49d5f6dc25b19a7c7e6d0388987a57db9684
Signer #1 public key MD5 digest: c015d8f0ebb1661ae2e7eecf3d0faf87
```

codery keystore（secrets 已在仓复用，未新建）；zipalign -P 16 页对齐后签名。证书指纹与 HG-2 线一致 → 与 v736 净化版互相可覆盖安装；覆盖装作者原版需先卸载。

## 5. Release `hg3b-round1-cc` 资产清单

| 资产 | 大小 | 说明 |
|---|---|---|
| hongguo-v7.3.7.32-clean-r1-cc.apk | 277,643,531 | 净化产物（不入 git） |
| patch-hg3b.log | 216 | 单点 patch 机器行 |
| MuteApplication.onCreate.diff | 435 | 点位 unified diff |
| verify-hg3b.txt | 951 | apksigner 全文 |
| verify-readback-hg3b.log | 301 | 回读三门 |
| sha256-hg3b.txt | 105 | CI sha 基线 |

## 6. 轮次与排障实录

- 首次触发 run 34894455632 秒败：workflow Release notes 串内手动换行破坏 `run: |` 块标量缩进（YAML 解析失败，GH 报 "workflow file issue"）。修复=b24e462 合入单行，二次触发即全绿。教训入库 context。
- v737 外层 Overlapped entries zip 在 `apktool d -f -r` 下正常解出（与 HG-3a unzip -o 实锤不冲突——apktool 走 java zip 读侧未触雷），门① 52 秒过。
- 重汇编实测 ~1.4 min（runner 快估），run 全程 3m36s。
- 构建轮号：CI 自增（grep Release `hg3b-round{N}-cc`），本轮 N=1；产物名/versionName 面三处一致由 Release 单源文件名保证（r1）。

## 7. 交接

装机实测归老马（本任务 MUST NOT 装机）。产物可从 Release `hg3b-round1-cc` 获取；复验命令：
`sha256sum hongguo-v7.3.7.32-clean-r1-cc.apk` == `598d6d28…8939f`。

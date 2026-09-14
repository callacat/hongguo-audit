# HG-3b 净化构建报告（Codex）

## 结论

- CI run `34900712742`：**success**。
- 构建触发 HEAD：`cb02f623fafe96c98a7b2ec09a499b406218626a`；证据回写 HEAD：`6f7f5d2`。
- Release：`hg3b-codex-r5`。
- Release asset：`hongguo-v7.3.7.32-clean-r5-codex.apk`。
- 产物 SHA-256：`64d47684adf515df05c151492fda3d2feff7f2f0315a602fe48b1fd061cb5685`。
- 产物大小：`277643531` bytes。
- 出处：`docs/hg3b/release-summary.txt`、`docs/hg3b/sha256.txt`。

## 输入校验

- 外层样本：`hongguo-v7.3.7.32-crack.apk`
- 外层 SHA-256：`337ff9417e672eb407ffd42481bd58eb33bea43ddd5762e1217f07597254b16e`
- 内层样本：`hongguo-73732-inner-official.apk`
- 内层 SHA-256：`a49cf486fb6c96d7b9169b3fa6a4a020295a8e46b78949b6b30fadc29b955bf9`
- 两个样本哈希均在 workflow 下载后强制校验。
- 出处：`.github/workflows/hongguo-clean-build-v737-codex.yml`、CI run `34900712742` 日志。

## 点位 diff

- 唯一修改点位：`smali_classes14/com/tencent/tinker/loader/MuteApplication.smali`。
- 原指令：`invoke-static {}, Lcom/b/a;->init()V`。
- 修改结果：删除该调用，并替换为 smali `nop`。
- patch 日志：`HG3B_PATCH_DONE files=1 invokes=1 lines=[1129]`。
- 家族类本体不删；回读确认 `com/b/a` 家族 3 个文件保留。
- 出处：`docs/hg3b/patch.log`、`docs/hg3b/point-diff.diff`、`docs/hg3b/reparse-gate.txt`。

```diff
--- a/smali_classes14/com/tencent/tinker/loader/MuteApplication.smali
+++ b/smali_classes14/com/tencent/tinker/loader/MuteApplication.smali
@@ -1126,7 +1126,8 @@
 .method public onCreate()V
     .locals 6

-    invoke-static {}, Lcom/b/a;->init()V
+    # HG3B-NOP-C: 断 invoke-static {} Lcom/b/a;->init()V（C 类设备指纹链入口）
+    nop

     const-string v0, "Mute.App"
```

## 双硬门

### 硬门 1：内层 `mod_src/assets/base.apk`

- 解包后的 `assets/base.apk` SHA-256 必须等于登记值 `a49cf486fb6c96d7b9169b3fa6a4a020295a8e46b78949b6b30fadc29b955bf9`。
- 构建前硬门通过：`HG3B_GATE1 inner_base_sha256=a49cf486...`。
- 签名后复测同值通过，且外层 dex 数保持 `24`。
- 出处：CI run `34900712742` 日志、`docs/hg3b/signed-gate.txt`。

### 硬门 2：产物重解回读

- 对签名产物再次 `apktool d -f -r`。
- `MuteApplication.onCreate()V` 内：`Lcom/b/a;->init()V` 为零。
- 同一方法内：`nop` 恰好 1 个。
- `com/b/a` 外部引用：`external_com_b_refs=0`。
- `com/b/a` 家族文件：`family_files=3`。
- 结果：`HG3B_GATE3 entry_nop=1 external_com_b_refs=0`、`HG3B_GATE3 family_files=3`、`HG3B_GATE3 PASS`。
- 出处：`docs/hg3b/reparse-gate.txt`。

## apksigner verify

- v1 scheme（JAR signing）：`true`
- v2 scheme：`true`
- v3 scheme：`true`
- v3.1 scheme：`false`
- v4 scheme：`false`
- SourceStamp：`false`
- signers：`1`
- signer certificate DN：`CN=Codery Debug, O=Codery, C=CN`
- signer certificate SHA-256：`bebb2cca93e02771751af4050a72a8a37986c3c052632a8aa715421d89ffc061`
- 出处：`docs/hg3b/verify.txt`。

## 保留范围

- A/B/D 全保留。
- 仅 C 家族入口 `MuteApplication.onCreate()V -> Lcom/b/a;->init()V` 断为 `nop`。
- 家族类本体 `com/b/a`、`com/b/a$Android_id`、`com/b/a$Reflect` 保留。
- 出处：`docs/hg3b/reparse-gate.txt`、`docs/hg3b/point-diff.diff`。

# HG-3 收口机械事实报告（Codex）

> 数据源：CI run `34888317725` artifact `hg3-codex-analysis-4`。分类判定权在老马。

## 1. 机械事实

| 项目 | 数字/结果 | 出处文件 |
|---|---:|---|
| 外层/内层官方类总数 | 290644 / 289416 | `analysis/diff-report.md` |
| 真新增类 | 1228 | `analysis/diff-report.md`、`analysis/dex-attribution.txt` |
| 真删除类 | 0 | `analysis/diff-report.md` |
| 修改类 | 3527 | `analysis/diff-report.md`、`analysis/dex-attribution.txt` |
| 修改类中差异方法 | 新增 14506 / 删除 30 / 修改 10408 | `analysis/diff-report.md` |
| 番茄画像重合率 | 1125 / 1218 = 92.4% | `analysis/diff-report.md` |
| 红果独有画像类 | 93 | `analysis/diff-report.md`、`hg-only-classes.txt` |
| 端点漂移 | URL 0 / IP 0 / 域名 27 | `analysis/endpoints.md` |
| C 家族存续 | 家族文件 0；引用文件 3；引用行 18 | `analysis/cba-scan.md` |
| `classes23` 归属 | unique=14791，added=0，changed=0，rearranged_official=14791 | `analysis/dex-attribution.txt` |
| `classes24` 归属 | unique=2102，added=0，changed=0，rearranged_official=2102 | `analysis/dex-attribution.txt` |
| HG-1 增量对比 | current_added=1228；hg1_baseline_added=1269；intersection=1135；new_vs_hg1=93；missing_vs_hg1=134 | `analysis/hg1-incremental.txt` |

## 2. 端点漂移明细

来源：`analysis/endpoints.md`。红果壳全集为 URL 0 / IP 0 / 域名 27；源报告将重合端点占比过低标记为“大漂移”。

```text
com.android.contacts
com.android.org.conscrypt.sslparametersimpl
com.bumptech.glide.generatedappglidemoduleimpl
com.bumptech.glide.load.model.stream.httpglideurlloader.timeout
com.bumptech.glide.load.resource.bitmap.bitmapencoder.compressionformat
com.bumptech.glide.load.resource.bitmap.bitmapencoder.compressionquality
com.bumptech.glide.load.resource.bitmap.centercrop
com.bumptech.glide.load.resource.bitmap.centerinside
com.bumptech.glide.load.resource.bitmap.downsampler.allowhardwaredecode
com.bumptech.glide.load.resource.bitmap.downsampler.decodeformat
com.bumptech.glide.load.resource.bitmap.downsampler.downsamplestrategy
com.bumptech.glide.load.resource.bitmap.downsampler.fixbitmapsize
com.bumptech.glide.load.resource.bitmap.downsampler.preferredcolorspace
com.bumptech.glide.load.resource.bitmap.fitcenter
com.bumptech.glide.load.resource.bitmap.videobitmapdecode.frameoption
com.bumptech.glide.load.resource.bitmap.videobitmapdecode.targetframe
com.bumptech.glide.load.resource.gif.gifoptions.decodeformat
com.bumptech.glide.load.resource.gif.gifoptions.disableanimation
com.bumptech.glide.manager
com.tencent.mobileqq
com.tencent.mobileqq.activity.jumpactivity
libcore.io.disklrucache
okhttpclient.class.getname
org.apache.harmony.xnet.provider.jsse.sslparametersimpl
org.eclipse.jetty.alpn.alpn
vnd.android.package
vnd.wap.wbmp
```

## 3. C 家族存续点位

来源：`analysis/cba-scan.md`。

- `classes14/com/tencent/tinker/loader/MuteApplication.smali`：line 1129 调用 `Lcom/b/a;->init()V`
- `classes23/com/b/a$Android_id.smali`：line 35 调用 `Lcom/b/a;->getReflect()Lcom/b/a$Reflect;` 与 `Lcom/b/a;->getID()Ljava/lang/String;`
- `classes23/com/b/a.smali`：line 23、27、33、35、39、168、176、195、203、208、210、217、251、257、289 存在字段读写或方法调用引用

## 4. HG-1 增量清单

来源：`analysis/hg1-incremental.txt`。以下先列 `new_vs_hg1` 93 项，再列 `missing_vs_hg1` 源清单 134 行（其中 88 个 `.smali` 项与 46 个路径前缀行）。

```text
an2/۟ۡۧۤۧ.smali
an2/۟ۢۢ۠ۦ.smali
an2/۟ۦۧۤ۟.smali
an2/۟ۦۨۢۤ.smali
an2/ۡۥ۠ۦ.smali
an2/ۥۣۣۢ.smali
an2/ۦۥۣ.smali
an2/ۧۢۧ۠.smali
an2/ۧۥۥۤ.smali
com/dragon/read/ad/util/۟ۢۢۤۤ.smali
com/dragon/read/ad/util/۟ۥۡۤۧ.smali
com/dragon/read/ad/util/۠۟ۦۤ.smali
com/dragon/read/ad/util/۠ۥۣ۟.smali
com/dragon/read/ad/util/ۡ۟ۤۢ.smali
com/dragon/read/ad/util/ۢۥۥۥ.smali
com/dragon/read/ad/util/ۢۧۦۦ.smali
com/dragon/read/ad/util/ۣۢۨۢ.smali
com/dragon/read/ad/util/ۦۨ۠ۥ.smali
com/dragon/read/ad/util/ۧۤ۠۠.smali
com/dragon/read/ad/util/ۧۦۤۤ.smali
com/dragon/read/base/ssconfig/model/۟۠ۨۨ۟.smali
com/dragon/read/base/ssconfig/model/۟ۡ۠ۧۢ.smali
com/dragon/read/base/ssconfig/model/ۣۣ۟۠۟.smali
com/dragon/read/base/ssconfig/model/ۣۣ۟ۤۨ.smali
com/dragon/read/base/ssconfig/model/۟ۦۤ۠۟.smali
com/dragon/read/base/ssconfig/model/ۤۨ۟۠.smali
com/dragon/read/base/ssconfig/model/ۥۦۥۦ.smali
com/dragon/read/base/ssconfig/model/ۦۤۨۦ.smali
com/dragon/read/component/biz/impl/mine/card/model/ۣ۟۠۠ۨ.smali
com/dragon/read/component/biz/impl/mine/card/model/۟ۤۡۨ۟.smali
com/dragon/read/component/biz/impl/mine/card/model/۠ۢۦ۠.smali
com/dragon/read/component/biz/impl/mine/card/model/ۢۥۡ.smali
com/dragon/read/component/biz/impl/mine/card/model/ۣۤۨ۟.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/ۣ۟ۢ۟.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/ۣ۟ۤۦۧ.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/۠۠ۥۡ.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/۠ۥۡۡ.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/ۢ۟ۦ۟.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/ۢۥۦۨ.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/ۣۨ.smali
com/dragon/read/component/biz/impl/mine/۠ۡ.smali
com/dragon/read/pages/main/ۣ۟ۡۥۤ.smali
com/dragon/read/pages/main/۟ۧۦ۟ۥ.smali
com/dragon/read/pages/main/ۤۢۨ.smali
com/dragon/read/pages/main/ۣۤۤۨ.smali
com/dragon/read/pages/main/ۤۦ۟ۡ.smali
com/dragon/read/pages/main/ۤۦۦۧ.smali
com/dragon/read/pages/main/ۧۨۦۦ.smali
com/dragon/read/polaris/۟ۡ۠ۢۧ.smali
com/dragon/read/polaris/۟ۢۦۦ.smali
com/dragon/read/polaris/۟ۧۢۥۨ.smali
com/dragon/read/polaris/ۡ۟ۢۡ.smali
com/dragon/read/polaris/ۣۢۧۨ.smali
com/dragon/read/polaris/ۤۥ۠ۨ.smali
com/dragon/read/polaris/ۧ۟ۡ۠.smali
com/dragon/read/polaris/ۨ۟۟ۡ.smali
com/dragon/read/reader/ad/noad/۟ۥۣۡۦ.smali
com/dragon/read/reader/ad/noad/۟ۧۡۧۤ.smali
com/dragon/read/reader/ad/noad/۟ۧۤۦۢ.smali
com/dragon/read/reader/ad/noad/ۡۦۧۡ.smali
com/dragon/read/reader/ad/noad/ۣۣۤۨ.smali
com/dragon/read/reader/ad/noad/ۦۢ۟ۡ.smali
com/dragon/read/reader/ad/۟ۡ۠ۧ۟.smali
com/dragon/read/reader/ad/۟ۤۡۢ۟.smali
com/dragon/read/reader/ad/ۡۡۤ۟.smali
com/dragon/read/reader/ad/ۣ۟ۦ۟.smali
com/dragon/read/reader/ad/ۥۢۨۡ.smali
com/dragon/read/reader/ad/ۧ۟۟ۦ.smali
com/dragon/read/reader/ad/ۣۨۢۧ.smali
com/dragon/read/rpc/rpc/۟۟ۥۢ۠.smali
com/dragon/read/rpc/rpc/۟ۧۡ۠ۦ.smali
com/dragon/read/rpc/rpc/ۣۥۢۡ.smali
com/dragon/read/user/model/۟۠۟۟ۡ.smali
com/dragon/read/user/model/۟۠ۤۧ۠.smali
com/dragon/read/user/model/۟ۡ۟۟ۨ.smali
com/dragon/read/user/model/۟ۢۦۥۨ.smali
com/dragon/read/user/model/۟ۧۤ۠ۤ.smali
com/dragon/read/user/model/۟ۧۦۦۦ.smali
com/dragon/read/user/model/ۣ۟ۥ۠.smali
com/dragon/read/user/model/ۤۢۢۧ.smali
com/dragon/read/util/۟۟۟ۧ۟.smali
com/dragon/read/util/ۣ۟ۢۢ۟.smali
com/dragon/read/util/ۣ۟ۤ۟ۧ.smali
com/dragon/read/util/۠ۤۦ۠.smali
com/dragon/read/util/ۢۡ۟ۦ.smali
com/dragon/read/util/ۥ۠ۧۢ.smali
com/j.smali
com/k.smali
com/pandora/core/۟۠ۥۧ۟.smali
com/pandora/core/ۣ۟ۢۢۡ.smali
com/pandora/core/ۣۥۨۤ.smali
com/ss/android/update/ۡ۠ۥۥ.smali
com/ss/android/update/ۣۨ۟.smali
```

```text
an2/
an2/۟۠ۢۥ.smali
an2/ۣ۟ۧۢۤ.smali
an2/۠ۤۦۣ.smali
an2/ۡۨۡۥ.smali
an2/ۣۣۥ۟.smali
an2/ۣۤۡۧ.smali
an2/ۧۨ۟۟.smali
com/
com/b/
com/dragon/
com/dragon/read/
com/dragon/read/ad/
com/dragon/read/ad/util/
com/dragon/read/ad/util/ۣۤۢ۟.smali
com/dragon/read/base/
com/dragon/read/base/ssconfig/
com/dragon/read/base/ssconfig/model/
com/dragon/read/base/ssconfig/model/۟۠ۢۢ.smali
com/dragon/read/base/ssconfig/model/۟ۤۦۨۧ.smali
com/dragon/read/base/ssconfig/model/۟ۥۡۨۧ.smali
com/dragon/read/base/ssconfig/model/ۣۡۨۥ.smali
com/dragon/read/base/ssconfig/model/ۣۤۢۦ.smali
com/dragon/read/base/ssconfig/model/ۤۧ۠ۦ.smali
com/dragon/read/base/ssconfig/model/ۥۡۢ۠.smali
com/dragon/read/base/ssconfig/model/ۣۣۧۤ.smali
com/dragon/read/component/
com/dragon/read/component/biz/
com/dragon/read/component/biz/impl/
com/dragon/read/component/biz/impl/mine/
com/dragon/read/component/biz/impl/mine/card/
com/dragon/read/component/biz/impl/mine/card/model/
com/dragon/read/component/biz/impl/mine/card/model/۟ۤۢۡۥ.smali
com/dragon/read/component/biz/impl/mine/card/model/۟ۥۥۣۡ.smali
com/dragon/read/component/biz/impl/mine/card/model/۟ۦۢۨۤ.smali
com/dragon/read/component/biz/impl/mine/card/model/ۣۣ۟ۧ۠.smali
com/dragon/read/component/biz/impl/mine/card/model/ۣ۟ۧۦ۟.smali
com/dragon/read/component/biz/impl/mine/card/model/۟ۧۤۢۤ.smali
com/dragon/read/component/biz/impl/mine/loginv2/
com/dragon/read/component/biz/impl/mine/loginv2/view/
com/dragon/read/component/biz/impl/mine/loginv2/view/۟۠ۥۦ۠.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/۟ۦ۠ۦۥ.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/۟ۧۧۥۨ.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/۠ۥۥ.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/ۣۡ۟ۥ.smali
com/dragon/read/component/biz/impl/mine/loginv2/view/ۤۦ۠ۡ.smali
com/dragon/read/component/biz/impl/mine/۟۟ۤۦۡ.smali
com/dragon/read/component/biz/impl/mine/۟ۢۥۣۢ.smali
com/dragon/read/component/biz/impl/mine/ۣ۟ۨۢۧ.smali
com/dragon/read/component/biz/impl/mine/۟ۦ۠ۢ۠.smali
com/dragon/read/component/biz/impl/mine/۟ۧۡۨۡ.smali
com/dragon/read/component/biz/impl/mine/ۣۣ.smali
com/dragon/read/pages/
com/dragon/read/pages/main/
com/dragon/read/pages/main/۟ۥۣۦۢ.smali
com/dragon/read/pages/main/۟ۥۦۧۥ.smali
com/dragon/read/pages/main/ۨۦۡۡ.smali
com/dragon/read/polaris/
com/dragon/read/polaris/۟۟۠ۥ.smali
com/dragon/read/polaris/۟۠ۦۨۢ.smali
com/dragon/read/polaris/۟۠ۧ۠۟.smali
com/dragon/read/polaris/۟ۢ۟ۡ۟.smali
com/dragon/read/polaris/ۣۣ۟۠۟.smali
com/dragon/read/polaris/۟ۤ۟۠ۥ.smali
com/dragon/read/polaris/ۣ۠ۨۨ.smali
com/dragon/read/polaris/ۧۢۨ۟.smali
com/dragon/read/reader/
com/dragon/read/reader/ad/
com/dragon/read/reader/ad/noad/
com/dragon/read/reader/ad/noad/۟۠ۥۤۢ.smali
com/dragon/read/reader/ad/noad/ۢۨۧۧ.smali
com/dragon/read/reader/ad/noad/ۤۥۧ۠.smali
com/dragon/read/reader/ad/۟ۦۣۣۣ.smali
com/dragon/read/reader/ad/ۣ۠ۢۨ.smali
com/dragon/read/reader/ad/ۣۡۨۧ.smali
com/dragon/read/reader/ad/ۢۨ۠ۡ.smali
com/dragon/read/reader/ad/ۤۢۢۤ.smali
com/dragon/read/reader/ad/ۤۥۧ.smali
com/dragon/read/reader/ad/ۦۣۧۢ.smali
com/dragon/read/rpc/
com/dragon/read/rpc/rpc/
com/dragon/read/rpc/rpc/ۣۣ۟۟ۤ.smali
com/dragon/read/rpc/rpc/۟ۡۦ۟ۥ.smali
com/dragon/read/rpc/rpc/ۣ۟ۧ۟ۡ.smali
com/dragon/read/rpc/rpc/۟ۧۦۡۥ.smali
com/dragon/read/rpc/rpc/ۡ۠ۤۧ.smali
com/dragon/read/rpc/rpc/ۣ۠ۤۦ.smali
com/dragon/read/rpc/rpc/ۨۦۤ.smali
com/dragon/read/user/
com/dragon/read/user/model/
com/dragon/read/user/model/۟ۤۧۢ.smali
com/dragon/read/user/model/۟ۥ۟ۦ.smali
com/dragon/read/user/model/۟ۦۣۢۡ.smali
com/dragon/read/user/model/۟ۧۦۣ.smali
com/dragon/read/user/model/ۦۣۣۧ.smali
com/dragon/read/util/
com/dragon/read/util/ۦۧۥۡ.smali
com/pandora/
com/pandora/core/
com/pandora/core/۟ۡۥۨ.smali
com/pandora/core/۟ۢۡ۠ۤ.smali
com/pandora/core/ۣ۟ۦ.smali
com/pandora/core/۟ۤ۠ۨ۠.smali
com/pandora/core/۟ۤۧۢۥ.smali
com/pandora/core/۟ۧۥۦۣ.smali
com/pandora/core/ۡۢۦۤ.smali
com/pandora/core/ۢۧ۠ۥ.smali
com/ss/
com/ss/android/
com/ss/android/update/
com/ss/android/update/۟۟ۤۤۡ.smali
com/ss/android/update/ۣۣ۟ۢۨ.smali
com/ss/android/update/۟ۤۡۡۤ.smali
com/ss/android/update/۟ۤۤۨۥ.smali
com/ss/android/update/۟ۥۧۦۣ.smali
com/ss/android/update/ۣۥۣۣ.smali
com/ss/android/update/ۣۣۨۨ.smali
com/ss/android/update/ۦۥ۠ۡ.smali
com/ss/android/update/ۧ۠ۧۨ.smali
com/ss/android/update/ۣۧ۟ۥ.smali
com/tZ.smali
com/ua.smali
org/
org/checkerframework/
org/checkerframework/checker/
org/checkerframework/checker/signature/
org/checkerframework/checker/signature/query/
org/checkerframework/checker/signature/query/security/
org/lsposed/
org/lsposed/hiddenapibypass/
org/lsposed/hiddenapibypass/library/
sgcore0/
sgcore0/hidden/
```

## 5. 分类建议（仅建议，判定权在老马）

- `A 候选`：1125 个与番茄画像重合类，建议按壳代码复核，出处 `analysis/diff-report.md`、`overlap-classes.txt`。
- `B/C/D 候选`：93 个红果独有画像类，建议老马结合行为与端点决定，出处 `analysis/diff-report.md`、`hg-only-classes.txt`。
- `C 重点`：`com/b/a` 虽无独立家族文件，但仍有 3 文件/18 行引用，建议列为存续点位，出处 `analysis/cba-scan.md`。
- `低倾向`：`classes23`、`classes24` 均为 rearranged_official，无 added/changed，出处 `analysis/dex-attribution.txt`。
- `端点倾向`：当前无 URL/IP 漂移；27 个“域名”多为字符串/配置噪声，判定权在老马，出处 `analysis/endpoints.md`。

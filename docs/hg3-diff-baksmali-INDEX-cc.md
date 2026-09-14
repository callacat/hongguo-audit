# hg3 baksmali 全文归档索引（v7.3.7.32，engine=cc；正文见 Release hg3-artifacts-cc 的 hg3-diff-baksmali.tar.gz）

- added 文件数: 1228

- changed 文件数: 3527

- removed 文件数: 0

- tar.gz 大小: 7.7M

## 差异方法最多的前 50 类（从报告 §3 表格截取）
```
|---|---|---|---|---|
| `com/dragon/read/pages/main/MainFragmentActivity.smali` | 1039 | 0 | 133 | 1172 |
| `com/dragon/read/util/DebugManager.smali` | 70 | 0 | 506 | 576 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2.smali` | 415 | 0 | 63 | 478 |
| `com/dragon/read/rpc/rpc/UgcApiService.smali` | 203 | 0 | 203 | 406 |
| `com/dragon/read/rpc/rpc/UserApiService.smali` | 179 | 0 | 179 | 358 |
| `com/dragon/read/reader/ad/ReaderAdManager.smali` | 299 | 0 | 35 | 334 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment.smali` | 189 | 0 | 41 | 230 |
| `com/dragon/read/pages/main/k2.smali` | 212 | 0 | 2 | 214 |
| `com/dragon/read/util/ImageLoaderUtils.smali` | 111 | 0 | 72 | 183 |
| `com/dragon/read/util/j4.smali` | 159 | 0 | 12 | 171 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment.smali` | 154 | 0 | 14 | 168 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment.smali` | 120 | 0 | 39 | 159 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2.smali` | 139 | 0 | 18 | 157 |
| `com/dragon/read/util/ApkSizeOptImageLoader.smali` | 131 | 0 | 9 | 140 |
| `com/dragon/read/util/j.smali` | 113 | 0 | 26 | 139 |
| `com/dragon/read/util/BookUtils.smali` | 56 | 0 | 77 | 133 |
| `com/ss/android/update/z.smali` | 66 | 24 | 42 | 132 |
| `com/dragon/read/ad/util/AdUtil.smali` | 115 | 0 | 10 | 125 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment.smali` | 88 | 0 | 28 | 116 |
| `com/ss/videoarch/liveplayer/VideoLiveManager.smali` | 0 | 0 | 116 | 116 |
| `com/dragon/read/pages/main/MainFragmentActivity$b0.smali` | 113 | 0 | 2 | 115 |
| `com/dragon/read/component/biz/impl/mine/card/model/QuickAccessCard.smali` | 93 | 0 | 15 | 108 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragment.smali` | 91 | 0 | 13 | 104 |
| `com/dragon/read/util/p8.smali` | 92 | 0 | 8 | 100 |
| `com/dragon/read/pages/main/k4.smali` | 71 | 1 | 21 | 93 |
| `an2/x0.smali` | 80 | 0 | 11 | 91 |
| `com/dragon/read/util/ToastUtils.smali` | 35 | 0 | 54 | 89 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment.smali` | 63 | 0 | 21 | 84 |
| `com/dragon/read/util/PictureUtils.smali` | 48 | 0 | 34 | 82 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity.smali` | 68 | 0 | 13 | 81 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineConfigImpl.smali` | 54 | 0 | 22 | 76 |
| `com/dragon/read/pages/main/w2.smali` | 70 | 0 | 5 | 75 |
| `com/ss/videoarch/liveplayer/log/LiveLoggerService.smali` | 0 | 0 | 74 | 74 |
| `com/dragon/read/pages/main/MainPageDrawerLayout.smali` | 7 | 0 | 61 | 68 |
| `com/ss/android/update/UpdateServiceImpl.smali` | 10 | 0 | 56 | 66 |
| `com/dragon/read/ad/util/u0.smali` | 42 | 0 | 22 | 64 |
| `com/ss/ttvideoengine/TTVideoEngineImpl.smali` | 0 | 0 | 64 | 64 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner.smali` | 0 | 0 | 63 | 63 |
| `com/dragon/read/util/BitmapUtils.smali` | 21 | 0 | 42 | 63 |
| `com/dragon/read/ad/util/c0.smali` | 55 | 0 | 7 | 62 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil.smali` | 54 | 0 | 7 | 61 |
| `com/dragon/read/pages/main/m.smali` | 57 | 0 | 4 | 61 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment.smali` | 36 | 0 | 24 | 60 |
| `com/dragon/read/component/biz/impl/mine/ProfileItemChangeActivity.smali` | 48 | 0 | 10 | 58 |
| `com/dragon/read/util/l2.smali` | 48 | 0 | 9 | 57 |
| `com/dragon/read/reader/ad/AdLine.smali` | 42 | 0 | 14 | 56 |
| `com/dragon/read/util/CdnLargeImageLoader.smali` | 40 | 0 | 16 | 56 |
| `com/dragon/read/util/j1.smali` | 24 | 0 | 32 | 56 |
| `com/dragon/read/component/biz/impl/mine/NewAboutActivity.smali` | 45 | 0 | 10 | 55 |
```

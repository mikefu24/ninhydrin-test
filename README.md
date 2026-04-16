# 🧪 茚三酮检测 - 移动应用

基于 Python + Kivy 的跨平台移动应用（Android + iOS）

## 📱 支持平台

- ✅ Android 5.0+
- ✅ iOS 12.0+
- ✅ 桌面（Windows/macOS/Linux）

## 🚀 快速开始

### 方式 1：使用构建好的 APK/IPA

```bash
# Android
adb install app-release.apk

# iOS
通过 Xcode 或 TestFlight 安装
```

### 方式 2：自行构建

```bash
# 安装依赖
pip install kivy kivymd

# 运行（桌面测试）
python main.py

# 构建 Android
buildozer android debug

# 构建 iOS
toolchain build python3 kivy
toolchain create <appname> <appdir>
```

## 📁 项目结构

```
ninhydrin_mobile/
├── main.py              # 主程序
├── ninhydrin_app.py     # 应用逻辑
├── analyzer.py          # 图像分析核心
├── buildozer.spec       # Android 构建配置
├── Info.plist           # iOS 配置
└── README.md            # 本文件
```

## 🎯 功能

- 📸 相机拍照分析
- 🖼️ 相册选择
- 🎨 颜色智能识别
- 📊 强度量化 (0-100)
- ✅ 结果判断
- 💡 操作建议
- 📚 历史记录
- 📥 数据导出

## 📋 系统要求

### Android
- Android 5.0 (API 21) 或更高
- 相机权限
- 存储权限

### iOS
- iOS 12.0 或更高
- 相机权限
- 照片库权限

## 🔧 开发说明

### 本地测试
```bash
pip install kivy kivymd pillow numpy
python main.py
```

### Android 构建
```bash
pip install buildozer
buildozer init
buildozer android debug
```

### iOS 构建
```bash
pip install kivy-ios
toolchain build python3 kivy pillow
toolchain create NinhydrinTest ~/path/to/app
```

## 📞 技术支持

如有问题，请检查：
- Python 版本 >= 3.7
- Kivy 版本 >= 2.0
- 相机权限已授予

---

**版本：** 1.0.0  
**开发时间：** 2026-04-16  
**适用：** 肽合成实验室茚三酮检测

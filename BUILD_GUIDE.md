# 🧪 茚三酮检测 App - APK 构建指南

## 📋 前提条件

- GitHub 账号
- Git 已安装
- 项目代码已准备好

---

## 方法 1：GitHub Actions（推荐）⭐

### 1. 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 仓库名：`ninhydrin-test`
3. 设为 **Public**（免费账号只能用 Public）
4. 点击 "Create repository"

### 2. 推送代码

```bash
cd /home/admin/.openclaw/workspace/ninhydrin_mobile

# 初始化 Git
git init

# 添加文件
git add -A

# 提交
git commit -m "🧪 Initial commit"

# 关联远程仓库（替换为你的用户名）
git remote add origin https://github.com/你的用户名/ninhydrin-test.git

# 推送
git branch -M main
git push -u origin main
```

### 3. 触发构建

推送后自动开始构建，或手动触发：

1. 访问：https://github.com/你的用户名/ninhydrin-test/actions
2. 点击 "Build Android APK"
3. 点击 "Run workflow" → "Run workflow"

### 4. 下载 APK

等待 60-90 分钟后：

1. 点击完成的构建记录
2. 页面底部 "Artifacts" → 点击 `ninhydrin-apk`
3. 下载并解压，得到 `.apk` 文件

### 5. 发布版本（可选）

```bash
# 创建版本标签
git tag v1.0.0
git push origin v1.0.0
```

APK 会自动发布到 Releases 页面。

---

## 方法 2：Docker 本地构建

### 前提条件

- Docker 已安装
- 至少 10GB 磁盘空间

### 构建步骤

```bash
cd /home/admin/.openclaw/workspace/ninhydrin_mobile

# 运行 Docker 构建
docker run --rm -v $(pwd):/home/user/hostcwd \
    -it kivy/buildozer android debug

# 输出位置：bin/ninhydrintest-1.0.0-debug.apk
```

### 构建 Release 版本

```bash
docker run --rm -v $(pwd):/home/user/hostcwd \
    -it kivy/buildozer android release
```

---

## 方法 3：本地 Buildozer（Ubuntu）

### 安装依赖

```bash
sudo apt-get update
sudo apt-get install -y \
    git ffmpeg cmake pkg-config \
    libjpeg-dev libffi-dev libssl-dev \
    libxml2-dev libxslt1-dev zlib1g-dev \
    libgstreamer1.0-dev gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    openjdk-11-jdk autoconf automake \
    build-essential libtool libtinfo5 \
    libncurses5 wget curl \
    python3-pip python3-setuptools \
    python3-dev

pip3 install buildozer Cython
```

### 构建

```bash
cd /home/admin/.openclaw/workspace/ninhydrin_mobile
buildozer android debug
```

---

## 📱 安装 APK

### 传输到手机

1. **微信/QQ**：发送 APK 到文件传输助手
2. **数据线**：直接拷贝到手机
3. **网盘**：上传后手机下载

### 安装步骤

1. 手机打开 APK 文件
2. 如果提示"未知来源"，点击"设置" → 允许
3. 点击"安装"
4. 完成！

---

## 🔧 常见问题

### Q: 构建失败 "SDK not found"

**A:** 首次构建会自动下载，耐心等待（约 20-30 分钟）

### Q: 构建超时

**A:** GitHub Actions 限时 90 分钟，如超时：
- 检查网络
- 使用 Docker 本地构建
- 重试构建

### Q: APK 无法安装

**A:** 
- 检查 Android 版本（需要 5.0+）
- 允许"未知来源"安装
- 重新下载完整 APK

### Q: 应用闪退

**A:** 
- 查看日志：`adb logcat | grep python`
- 检查权限设置
- 重新构建 debug 版本测试

---

## 📊 构建时间参考

| 方式 | 首次构建 | 后续构建 |
|------|---------|---------|
| GitHub Actions | 60-90 分钟 | 30-50 分钟 |
| Docker | 40-60 分钟 | 20-30 分钟 |
| 本地 Buildozer | 40-60 分钟 | 20-30 分钟 |

---

## 📦 APK 大小

- Debug 版本：约 30-40 MB
- Release 版本：约 20-30 MB

---

## 🎯 下一步

构建成功后：

1. ✅ 测试基本功能
2. ✅ 拍照分析测试
3. ✅ 历史记录测试
4. ✅ 收集用户反馈
5. ✅ 优化并构建 Release 版本

---

**技术支持：** 如有问题，查看 GitHub Actions 日志或联系开发者

# 📱 添加 App 图标指南

## 当前状态

✅ 已配置 `buildozer.spec` 使用 `icon.png`

⚠️ 需要手动添加图标文件

---

## 方式 A：使用 ImageMagick（推荐）

```bash
# 安装 ImageMagick
sudo apt-get install imagemagick

# 生成图标
cd /home/admin/.openclaw/workspace/ninhydrin_mobile
convert -size 512x512 xc:'#8B2E9B' -fill white \
  -draw "circle 256,256 256,0" \
  -fill white -gravity center -pointsize 200 \
  -annotate 0 "N" \
  icon.png
```

---

## 方式 B：使用在线工具

1. 访问：https://www.canva.com/icons/
2. 创建 512x512 图标
3. 下载为 PNG
4. 保存到项目根目录，命名为 `icon.png`

---

## 方式 C：使用现有 PNG

任何 512x512 PNG 文件，重命名为 `icon.png` 放到项目根目录

---

## 添加图标后

```bash
cd /home/admin/.openclaw/workspace/ninhydrin_mobile
git add icon.png
git commit -m "🎨 添加 App 图标"
git push
```

GitHub Actions 会自动重新构建带图标的 APK！

---

## 图标设计规范

- **尺寸**: 512x512 px
- **格式**: PNG（透明背景）
- **颜色**: 紫红色（茚三酮反应色）#8B2E9B
- **主题**: 化学/检测相关

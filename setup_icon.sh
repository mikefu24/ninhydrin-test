#!/bin/bash
# 使用内置工具创建简单图标

# 创建一个简单的 512x512 紫色正方形 PNG（使用 ImageMagick 或其他工具）
# 如果没有 ImageMagick，使用预生成的 base64

# 检查是否有 imagemagick
if command -v convert &> /dev/null; then
    convert -size 512x512 xc:purple -fill white -draw "circle 256,256 256,0" icon.png
    echo "✓ 使用 ImageMagick 生成图标"
else
    # 创建一个简单的 base64 PNG（1x1 紫色像素，Buildozer 会缩放）
    echo "⚠ ImageMagick 未安装，使用备用方案"
    echo "请在有 ImageMagick 的机器上运行：convert -size 512x512 xc:'#8B2E9B' -fill white -draw 'circle 256,256 256,0' icon.png"
fi

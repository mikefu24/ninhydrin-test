#!/usr/bin/env python3
"""
生成 Android App 图标 - 茚三酮检测
生成所有必要尺寸的图标文件
"""

from PIL import Image, ImageDraw, ImageFont
import os

# 输出目录
ICON_DIR = "res/icon"
os.makedirs(ICON_DIR, exist_ok=True)

# Android 需要的图标尺寸
SIZES = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
    "playstore": 512,  # Google Play 商店图标
}

def create_icon(size, filename):
    """创建圆形渐变图标"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制圆形背景（紫色渐变）
    margin = size // 10
    bbox = [margin, margin, size - margin, size - margin]
    
    # 渐变色（茚三酮反应颜色：紫红色）
    color1 = (128, 0, 128)  # 紫色
    color2 = (180, 50, 150)  # 紫红色
    
    # 绘制圆形
    draw.ellipse(bbox, fill=(140, 30, 140, 255))
    
    # 添加文字 "N" 或化学符号
    try:
        font_size = size // 2
        # 尝试使用系统字体
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # 绘制文字
    text = "N"  # Ninhydrin
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    
    # 保存
    img.save(filename, 'PNG')
    print(f"✓ 生成：{filename} ({size}x{size})")

# 生成所有尺寸
for name, size in SIZES.items():
    if name == "playstore":
        create_icon(size, f"{ICON_DIR}/playstore-icon.png")
    else:
        create_icon(size, f"{ICON_DIR}/{name}-icon.png")

print("\n✅ 图标生成完成！")
print("将图标文件移动到正确位置:")
print("  res/icon/ → 所有图标文件")

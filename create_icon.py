#!/usr/bin/env python3
"""生成简单的 PNG 图标"""

from PIL import Image, ImageDraw

def create_icon(size, filename):
    """创建茚三酮检测图标"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 圆形背景（紫红色）
    margin = size // 10
    bbox = [margin, margin, size - margin, size - margin]
    draw.ellipse(bbox, fill=(140, 30, 140, 255))
    
    # 绘制简单的试管形状
    tube_top = size // 3
    tube_bottom = size * 2 // 3
    tube_width = size // 6
    tube_x = size // 2 - tube_width // 2
    
    # 试管主体
    draw.rectangle(
        [tube_x, tube_top, tube_x + tube_width, tube_bottom],
        fill=(255, 255, 255, 230),
        outline=(200, 200, 200, 255)
    )
    
    # 试管口
    draw.rectangle(
        [tube_x - 5, tube_top - 10, tube_x + tube_width + 5, tube_top],
        fill=(255, 255, 255, 230)
    )
    
    # 液体（紫红色）
    liquid_top = tube_top + 15
    draw.rectangle(
        [tube_x + 3, liquid_top, tube_x + tube_width - 3, tube_bottom - 5],
        fill=(200, 80, 200, 180)
    )
    
    # 保存
    img.save(filename, 'PNG')
    print(f"✓ {filename} ({size}x{size})")

# 生成主图标
create_icon(512, "icon.png")
print("\n✅ 图标生成完成！")

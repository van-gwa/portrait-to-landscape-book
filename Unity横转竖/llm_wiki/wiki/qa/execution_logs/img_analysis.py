# -*- coding: utf-8 -*-
import sys
import os
from PIL import Image

dir_path = r'D:\CursorProject\Dadian - 副本\Arts\Doc\UIImage'
file_name = 'UI_BattlePassRewardOverview.png'
full_path = os.path.join(dir_path, file_name)

img = Image.open(full_path)
pixels = img.load()
w, h = img.width, img.height

# Analyze vertical sections (top/middle/bottom)
sections = {
    'top': (0, h//4),
    'middle_top': (h//4, h//2),
    'middle_bottom': (h//2, 3*h//4),
    'bottom': (3*h//4, h)
}

for name, (y1, y2) in sections.items():
    non_black = 0
    for y in range(y1, y2):
        for x in range(w):
            r, g, b = pixels[x, y][:3]
            if not (r < 20 and g < 20 and b < 20):  # not near black
                non_black += 1
    total = w * (y2 - y1)
    ratio = non_black / total * 100
    print(f"{name}: {non_black}/{total} = {ratio:.1f}%")

# Check center area for content
center_y1, center_y2 = h//4, 3*h//4
center_content = 0
for y in range(center_y1, center_y2):
    for x in range(w//4, 3*w//4):  # center region
        r, g, b = pixels[x, y][:3]
        if not (r < 30 and g < 30 and b < 30):
            center_content += 1

print(f"Center region content: {center_content}")

# Check if there's a clear horizontal layout (rows of items)
# Sample middle section for horizontal patterns
row_height = h // 10
for i in range(5):
    y = h//4 + i * row_height
    non_black_in_row = 0
    for x in range(w):
        r, g, b = pixels[x, y][:3]
        if not (r < 20 and g < 20 and b < 20):
            non_black_in_row += 1
    ratio = non_black_in_row / w * 100
    print(f"Row {i}: y={y}, density={ratio:.1f}%")

img.close()
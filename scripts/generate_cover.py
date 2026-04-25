from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pathlib import Path

W, H = 900, 383
img = Image.new('RGB', (W, H), '#0b1020')
draw = ImageDraw.Draw(img)

# gradient background
for y in range(H):
    t = y / H
    r = int(11 + (18-11)*t)
    g = int(16 + (28-16)*t)
    b = int(32 + (52-32)*t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# soft glows
for box, color in [((40, 40, 360, 320), (38, 82, 255, 90)), ((540, 20, 880, 340), (0, 212, 170, 70)), ((260, 170, 760, 420), (120, 60, 255, 55))]:
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.ellipse(box, fill=color)
    layer = layer.filter(ImageFilter.GaussianBlur(50))
    img = Image.alpha_composite(img.convert('RGBA'), layer)
img = img.convert('RGB')
draw = ImageDraw.Draw(img)

# grid lines
for x in range(0, W, 60):
    draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 12), width=1)
for y in range(0, H, 48):
    draw.line([(0, y), (W, y)], fill=(255, 255, 255, 10), width=1)

# cards / panels
panel = (36, 28, 864, 347)
draw.rounded_rectangle(panel, radius=24, fill=(10, 14, 26), outline=(255, 255, 255, 28), width=2)

overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
od.rounded_rectangle((52, 46, 520, 326), radius=18, fill=(255,255,255,14), outline=(255,255,255,24), width=1)
od.rounded_rectangle((560, 58, 838, 300), radius=18, fill=(255,255,255,10), outline=(255,255,255,18), width=1)
overlay = overlay.filter(ImageFilter.GaussianBlur(0))
img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
draw = ImageDraw.Draw(img)

# font discovery
font_candidates = [
    '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc',
    '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
    '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
]
font_path = next((p for p in font_candidates if Path(p).exists()), None)
if not font_path:
    raise SystemExit('No usable font found')

font_title = ImageFont.truetype(font_path, 52)
font_sub = ImageFont.truetype(font_path, 22)
font_tag = ImageFont.truetype(font_path, 18)
font_big = ImageFont.truetype(font_path, 40)

# small top label
label = 'AI 组织观察'
draw.rounded_rectangle((72, 68, 198, 100), radius=16, fill=(47, 111, 237))
draw.text((90, 74), label, font=font_tag, fill=(255, 255, 255))

# title
x0, y0 = 76, 122
lines = ['老板的幻觉', '在AI之上']
for i, line in enumerate(lines):
    draw.text((x0, y0 + i * 68), line, font=font_title, fill=(245, 248, 255))

# underline accent
accent_y = y0 + 146
for i, c in enumerate([(47,111,237), (0,212,170), (171,113,255)]):
    draw.rounded_rectangle((78 + i*92, accent_y, 148 + i*92, accent_y + 8), radius=4, fill=c)

# subtitle
sub = '不是AI在骗老板\n是老板先把欲望投射给了AI'
draw.multiline_text((78, 286), sub, font=font_sub, fill=(173, 186, 214), spacing=8)

# right side visual metaphor: speech bubble + crown + glitch bars
# speech bubble
rb = (598, 86, 806, 198)
draw.rounded_rectangle(rb, radius=22, fill=(20, 28, 48), outline=(117, 141, 255), width=2)
draw.polygon([(674, 198), (698, 198), (684, 220)], fill=(20, 28, 48), outline=(117, 141, 255))
draw.text((630, 116), '你是对的', font=font_big, fill=(237, 242, 255))

# crown
crown = [(630, 246), (652, 210), (682, 244), (716, 204), (748, 244), (780, 214), (798, 246), (798, 270), (630, 270)]
draw.polygon(crown, fill=(255, 196, 78), outline=(255, 226, 143))
for cx in [652, 716, 780]:
    draw.ellipse((cx-5, 228-5, cx+5, 228+5), fill=(255, 245, 200))

draw.rounded_rectangle((630, 276, 798, 286), radius=4, fill=(255, 196, 78))

# glitch bars
for i, yy in enumerate([92, 122, 152, 182, 300, 324]):
    color = [(47,111,237), (0,212,170), (171,113,255)][i % 3]
    draw.rounded_rectangle((820, yy, 846, yy + 8), radius=4, fill=color)

# bottom note
note = 'Khazix Writer / 封面草案'
draw.text((650, 314), note, font=font_tag, fill=(129, 144, 173))

out = '/workspace/output/老板的幻觉在AI之上_公众号封面.png'
img.save(out)
print(out)

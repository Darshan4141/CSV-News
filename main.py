# ----------- Modules -----------
from PIL import Image, ImageDraw, ImageFont
import textwrap

# ----------- Init -----------
size_w, size_h = 500, 500
image = Image.new("RGB", (size_w, size_h), (255, 255, 255))

alan = Image.open("alan_turing.png")
alan_w, alan_h = alan.size

# ----------- Alan Image -----------
upper_height = 100
crop_area_h = 150
box = ((alan_w - size_w) // 2, upper_height, (alan_w - size_w) // 2 + size_w, upper_height + size_h - crop_area_h)

image.paste(alan.crop(box))

# ----------- Logo -----------
circle_dia = 80
left_padding = 20
up_padding = 10

m_logo = Image.open("csv_logo_white.jpg")
logo = m_logo.resize((circle_dia, circle_dia))

mask_im = Image.new("L", logo.size, 0)
draw = ImageDraw.Draw(mask_im)

circle_box = (0, 0, circle_dia, circle_dia)
draw.ellipse(circle_box, fill=255)

logo_box = (left_padding, up_padding, circle_dia + left_padding, circle_dia + up_padding)
# logo_box = (size_w - (circle_dia) - padding, padding, size_w - padding, (circle_dia) + padding)
image.paste(logo, logo_box, mask_im)

# ----------- Polygon -----------
up_dist = 320
width = 80
height = 60
delta = 20
xy = [
    (width + delta, up_dist),
    (size_w - width + delta, up_dist),
    (size_w - width - delta, up_dist + height),
    (width - delta, up_dist + height),
]

final = ImageDraw.Draw(image)
final.polygon(xy, fill=("#c7372f"))

# ----------- Text -----------
# ----- Top left -----


# ----- Middle Center -----
offset = 10
font = ImageFont.truetype("GEORGIAB.TTF", 45)
name = "Alan Turing"
w, h = draw.textsize(name, font=font)
final.text(((size_w - w) // 2, up_dist + (height - h) // 2), name, font=font, fill=(255, 255, 255))

# ----- Bottom Center -----
padding = 20
bottom_dist = 100
font = ImageFont.truetype("GEORGIA.TTF", 25)
text = "In 1936, he developed the idea for the Universal Turing Machine, the basis for the first computer."
para = textwrap.wrap(text, width=20)
print(para)

final.multiline_text((padding, size_h - bottom_dist), para, font=font, fill=(0, 0, 0))


# ----------- Driver Code -----------
image.show()



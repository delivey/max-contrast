from PIL import Image, ImageColor, ImageEnhance
from helpers import GetIntensityByte, ClampToByte

og = Image.open("./256.png")
pixels = og.load()

brightness = 0
contrast = -100

if contrast < 0:
    multiply = contrast + 100
    divide = 100
elif contrast > 0:
    multiply = 100
    divide = 100 - contrast
else:
    multiply = 1
    divide = 1

for i in range(og.size[0]):
    for j in range(og.size[1]):
        colors = pixels[i, j][0:3]
        intensity = GetIntensityByte(colors)
        if divide == 0:
            if intensity+brightness < 128:
                og.putpixel((i, j), (0, 0, 0))
            else:
                og.putpixel((i, j), (255, 255, 255))
        elif divide == 100:
            shift = (intensity - 127 + brightness) * multiply / divide + 127 - intensity
            R = ClampToByte(colors[0] + shift)
            G = ClampToByte(colors[1] + shift) 
            B = ClampToByte(colors[2] + shift)
            og.putpixel((i, j), (R, G, B))

og.show()


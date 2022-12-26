from PIL import Image, ImageColor, ImageEnhance

og = Image.open("./256.png")
pixels = og.load()

brightness = 0
contrast = 100

if contrast < 0:
    multiply = contrast + 100
    divide = 100
elif contrast > 0:
    multiply = 100
    divide = 100 - contrast
else:
    multiply = 1
    divide = 1


# Returns: A value in the range 0 to 255 inclusive.
def GetIntensityByte(rgb):
    return (7471 * rgb[2] + 38470 * rgb[1] + 19595 * rgb[0]) >> 16

for i in range(og.size[0]):  # for every pixel:
    for j in range(og.size[1]):
        colors = pixels[i, j][0:3]  # r g b

        if GetIntensityByte(colors) < 128:
            og.putpixel((i, j), (0, 0, 0))
        else:
            og.putpixel((i, j), (255, 255, 255))

og.show()


from PIL import Image, ImageColor, ImageEnhance

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

def ClampToByte(x): 
    if x > 255:
        return 255
    elif x < 0:
        return 0
    return int(x)

rgbTable = []
for i in range(256**2):
    rgbTable.append(0)

# Returns: A value in the range 0 to 255 inclusive.
def GetIntensityByte(rgb):
    return (7471 * rgb[2] + 38470 * rgb[1] + 19595 * rgb[0]) >> 16

if divide == 100:
    for intensity in range(256):
        shift = (intensity - 127 + brightness) * multiply / divide + 127 - intensity;

        for col in range(256):
            index = (intensity * 256) + col
            rgbTable[index] = ClampToByte(col + shift)

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
            inten = GetIntensityByte(colors)

            shiftIndex = inten * 256

            R = rgbTable[shiftIndex + colors[0]]
            G = rgbTable[shiftIndex + colors[1]]
            B = rgbTable[shiftIndex + colors[2]]

            og.putpixel((i, j), (R, G, B))

og.show()


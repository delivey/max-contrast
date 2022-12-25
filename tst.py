from PIL import Image, ImageColor, ImageEnhance

og = Image.open("./256.png")
pixels = og.load()

for i in range(og.size[0]):  # for every pixel:
    for j in range(og.size[1]):
        colors = pixels[i, j][0:3]  # r g b

        if (sum(colors) / 3) < 128:
            og.putpixel((i, j), (0, 0, 0))
        else:
            og.putpixel((i, j), (255, 255, 255))

og.show()
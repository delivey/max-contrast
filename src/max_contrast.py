from PIL import Image

def contrast_image(image_path, brightness, contrast, save_path=False, show=False):
    # Returns: A value in the range 0 to 255 inclusive.
    def GetIntensityByte(rgb):
        return (7471 * rgb[2] + 38470 * rgb[1] + 19595 * rgb[0]) >> 16

    # Returns: A normalized color between 0 to 255
    def ClampToByte(x): 
        if x > 255:
            return 255
        elif x < 0:
            return 0
        return int(x)

    img = Image.open(image_path)
    pixels = img.load()

    if contrast < -100: contrast = -100
    if contrast > 100: contrast = 100

    if brightness < -100: brightness = -100
    if brightness > 100: brightness = 100

    if contrast < 0:
        multiply = contrast + 100
        divide = 100
    elif contrast > 0:
        multiply = 100
        divide = 100 - contrast
    else:
        multiply = 1
        divide = 1

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            colors = pixels[i, j][0:3]
            intensity = GetIntensityByte(colors)
            if divide == 0:
                if intensity+brightness < 128:
                    img.putpixel((i, j), (0, 0, 0))
                else:
                    img.putpixel((i, j), (255, 255, 255))
                continue
            elif divide == 100:
                shift = (intensity - 127) * multiply / divide + 127 - intensity + brightness
            else:
                shift = (intensity - 127 + brightness) * multiply / divide + 127 - intensity
            R = ClampToByte(colors[0] + shift)
            G = ClampToByte(colors[1] + shift) 
            B = ClampToByte(colors[2] + shift)
            img.putpixel((i, j), (R, G, B))

    if show:
        img.show()

    if save_path:
        img.save(save_path)
        return True
    else:
        return img
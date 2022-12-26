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

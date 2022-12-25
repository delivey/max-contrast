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

rgbTable = []
for i in range(256**2):
    rgbTable.append(0)

if divide == 0:
    for intensity in range(256):
        if intensity + brightness < 128:
            rgbTable[intensity] = 0
        else:
            rgbTable[intensity] = 255

print(rgbTable)
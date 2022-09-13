from PIL import Image

im = Image.open("1.jpg")
pixelMap = im.load()
img = Image.new(im.mode, im.size)
pixelsNew = img.load()
pm = pixelMap
count = 0
for i in range(img.size[0]):
    for j in range(img.size[1]):
        c = pm[i,j]
        if c[0] > 254:
            pixelsNew[i, j] = c
            count += 1
            print(f'{c}')
        else:
            pixelsNew[i, j] = (0, 0, 0)
    pixelMap[i, j] = pixelsNew[i, j]
img.show()
# requires PIL (python image library)
from PIL import Image

im = Image.open("1.jpg")  # replace with the image file name in your directory
pixelMap = im.load()
img = Image.new(im.mode, im.size)
pixelsNew = img.load()
pm = pixelMap

# looping through the image row by row & column by column
for i in range(img.size[0]):
    for j in range(img.size[1]):
        c = pm[i,j]
        r = c[0]
        b = c[1]
        g = c[2]
        if [r, g, b] == [200, 20, 130]:  # Replace this line with whatever boolean you'd like
            pixelsNew[i,j] = c
            print(f"{[i,j]}")   # prints the coordinates
pixelMap[i, j] = pixelsNew[i, j]
img.show()  # shows the new image

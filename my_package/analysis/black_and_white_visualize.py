from my_package.model import InstanceSegmentationModel
import numpy as np
from matplotlib.pyplot import *
import PIL
from PIL import Image

def change_shape(ar):
    height=len(ar)
    width=len(ar[0])
    li=np.empty((3,height,width))
    for h in range(height):
        for w in range(width):
            for c in range(3):
                li[c][h][w]=ar[h][w][c]
    return li

def plot_visualization(img_dir): # Write the required arguments
    img_dir = r"{}".format(img_dir)
    image = Image.open(img_dir)
    image.convert('RGB')
    width,height = image.size

    ar1 = np.array(image)
    ar1 = ar1 / 255
    ar = change_shape(ar1)

    ism = InstanceSegmentationModel()
    li = ism(ar)


    sar = li[1] # segmentation mask
    far = np.zeros([height, width])
    c = 0
    for a in sar:
        far += a[0]
        c += 1
        if (c == 3): break

    for row in range(height):
        for col in range(width):
            far[row][col] = max(1 - far[row][col], 0)
            s = 0
            for c in range(3):
                s += ar[c][row][col]
            s = s / 3
            f = far[row][col]
            if f < 0.45:
                x = 0
            else:
                if s < 0.25:
                    x = 0.2
                elif s < 0.75:
                    x = 0.4
                else:
                    x = 1
            far[row][col] = x


    bbx = li[0]

    for i in range(min(3,len(bbx))):
        e = bbx[i]
        a, b = e[0]
        c, d = e[1]

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        for x in range(a, c):
            far[b][x] = 0
            far[d][x] = 0

        for y in range(b, d):
            far[y][a] = 0
            far[y][c] = 0

    img = Image.fromarray(np.uint8(far * 255), 'L')

    label = li[2]
    prob = li[3]
    draw = PIL.ImageDraw.Draw(img)

    for i in range(min(3,len(bbx))):
        e = bbx[i]
        a, b = e[0]
        c, d = e[1]

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        text = label[i] + ' ' + str(prob[i])[:4]
        draw.text((a + 2, b - 10), text, fill="black", align="left")
    img.show()

  # The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.

plot_visualization(r"C:\Users\Gaurav Malakar\PycharmProjects\Machine_Learning\Python_DS_Assignment\data\imgs\3.jpg")

import numpy as np
from matplotlib.pyplot import *
import PIL
from PIL import Image


def apply_mask(ar, mask, color, height, width):
    for h in range(height):
        for w in range(width):
            if mask[h][w] > 0.75: ar[h][w] = color
    return


def apply_bbox(ar, bbox, height, width,fill,color):
    a, b = bbox[0]
    c, d = bbox[1]

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    pix = 0
    color_sum = 0
    for h in range(max(b-10,2),max(b-1,2)):
        for w in range(a+1,min(a+13,width-1)):
            color_sum += (ar[h][w][0] + ar[h][w][1] + ar[h][w][2])/3
            pix+=1
    color_sum=color_sum/max(pix,1)



    if color_sum < 0.5: fill.append('white')
    else: fill.append('black')



    for x in range(a+1, c-1):
        ar[b+1][x] = ar[d-1][x] = color

    for y in range(b+1, d-1):
        ar[y][a+1] = ar[y][c-1] = color
    return


def apply_label(img, li, fill, n):
    label = li[2]
    prob = li[3]
    bbox_list = li[0]
    draw = PIL.ImageDraw.Draw(img)

    for i in range(n):
        bbox = bbox_list[i]
        a, b = bbox[0]
        c, d = bbox[1]
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        text = label[i] + ' (' + str(prob[i])[:4] + ')'
        draw.text((a, max(b - 10,2)), text, fill=fill[i], align="left")




def plot_visualization(prediction_list,image_array,output_folder=None,type='both'):  # ar.shape = (H,W,3)
    height = len(image_array)
    width = len(image_array[0])

    mask_list = prediction_list[1]  # segmentation mask
    color_list = np.array(
        [np.array([1, 1, 0]), np.array([128 / 255, 1, 0]), np.array([0, 1, 1])])  # list of colors used for masking

    n = len(mask_list)  # number of entities identified by the model
    n = min(n, 3)
    fill=[]
    for i in range(n):
        if type!='bounding_box':
            mask = mask_list[i][0]
            apply_mask(image_array, mask, color_list[i], height, width)
        if type!='segmentation':
            bbox = prediction_list[0][i]
            apply_bbox(image_array, bbox, height, width, fill,color_list[i])

    img = Image.fromarray(np.uint8(image_array * 255))
    if type!='segmentation':
        apply_label(img, prediction_list, fill, n)

    if output_folder==None: return img
    else: img.save(output_folder,'JPEG')


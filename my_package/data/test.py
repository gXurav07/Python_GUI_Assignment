# Imports
from my_package.model import InstanceSegmentationModel
from my_package.analysis.visualize import plot_visualization
import os
import numpy as np
from matplotlib.pyplot import *
import PIL
from PIL import Image
import json

image = Image.open(r"C:\Users\Gaurav Malakar\PycharmProjects\Machine_Learning\Python_DS_Assignment\data\imgs\9.jpg")
image.convert('RGB')
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
width,height=image.size
print(height,width)

ar = np.array(image)
ar = ar/255

ar = ar.transpose(2,0,1)
ism = InstanceSegmentationModel()
li = ism(ar)
ar = ar.transpose(1,2,0)
outputs = r"C:\Users\Gaurav Malakar\PycharmProjects\Machine_Learning\Outputs\visualized.jpg"
plot_visualization(li,ar,outputs)

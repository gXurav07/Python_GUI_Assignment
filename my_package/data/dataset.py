import os
import numpy as np
from matplotlib.pyplot import *
import PIL
from PIL import Image
import json

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''
    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.file = open(annotation_file)
        self.transforms = transforms
        self.flist=[]
        self.dir = str(os.getcwd())

        for line in self.file:
            data = json.loads(line)
            self.flist.append(data)

    def __len__(self):
        return len(self.flist)
        '''
            return the number of data points in the dataset
        '''

    def getitem(self, idx):
        datapoint = self.flist[idx-1]

        dict = {}

        loc = self.dir + '\\data\\' + datapoint['img_fn'].replace('/','\\')
        loc = r"{}".format(loc)
        image = Image.open(loc)

        seg_loc = self.dir + '\\data\\' +  datapoint['png_ann_fn'].replace('/','\\')
        seg_loc = r"{}".format(seg_loc)
        seg_image = Image.open(seg_loc)

        if (self.transforms!=None):
            for transformation in self.transforms:
                print(transformation.new_dimensions, transformation.crop_type)
                image = transformation(image)


        ar = np.array(image)
        ar = ar/255
        ar = ar.transpose(2,0,1)
        dict['image'] = ar


        seg_ar = np.array(seg_image)
        seg_ar = seg_ar/255
        seg_ar = np.array([seg_ar])
        dict['gt_png_ann'] = seg_ar

        item_list = datapoint['bboxes'] # bounding box list

        bbox_list=[]


        for item in item_list:
            box = np.array([item['category']] + item['bbox'],dtype=object)
            bbox_list.append(box)
        bbox_list = np.array(bbox_list,dtype = object)


        dict['gt_bboxes'] = bbox_list

        return dict


        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_png_ann: the segmentation annotation image (in the form of a numpy array) (shape: (1, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image, png segmentation and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the arrays would be (3, H, W) and (1, H, W), respectively.
            3. Scale the values in the arrays to be with [0, 1].
            4. Perform the desired transformations on the image. *****
            5. Return the dictionary of the transformed image and annotations as specified.
        '''





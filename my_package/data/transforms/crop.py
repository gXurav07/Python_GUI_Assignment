# Imports
from random import randrange



class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        # Write your code here
        self.new_dimensions = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        prev_size = image.size

        if self.crop_type == 'random':
            w = randrange(0, prev_size[0] - self.new_dimensions[0])
            h = randrange(0, prev_size[1] - self.new_dimensions[1])
            return image.crop((w, h, w + self.new_dimensions[0], h + self.new_dimensions[1]))
        elif self.crop_type == 'center':
            l_idx = (prev_size[0] - self.new_dimensions[0]) / 2
            t_idx = (prev_size[1] - self.new_dimensions[1]) / 2
            r_idx = (prev_size[0] + self.new_dimensions[0]) / 2
            d_idx = (prev_size[1] + self.new_dimensions[1]) / 2

            cropped_img = image.crop((l_idx, t_idx, r_idx, d_idx))
            
            return cropped_img

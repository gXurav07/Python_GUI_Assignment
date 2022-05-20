# Imports
from PIL import ImageOps


class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # Write your code here
        self.flip_axis = flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        if self.flip_axis == "horizontal":
            flipped_img = ImageOps.mirror(image)
        elif self.flip_axis == "vertical":
            flipped_img = ImageOps.flip(image)
        
        return flipped_img

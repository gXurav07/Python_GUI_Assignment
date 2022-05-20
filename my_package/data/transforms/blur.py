# Imports
from PIL import ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius=1):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        # Write your code here
        self.blur_radius = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        # Write your code here
        blurred_img =  image.filter(ImageFilter.GaussianBlur(self.blur_radius))
        return blurred_img

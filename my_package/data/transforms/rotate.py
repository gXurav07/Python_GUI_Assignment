# Imports
from PIL import Image


class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.   ( positive: anticlockwise/left)
        '''

        # Write your code here
        self.degOfRotation = degrees

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        rotated_img =  sample.rotate(self.degOfRotation)

        return rotated_img

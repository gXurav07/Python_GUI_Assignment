# Imports
from PIL import Image


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        self.new_dimensions = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here
        current_size = image.size
        width = current_size[0]
        height = current_size[1]

        if type(self.new_dimensions) == int:
            if width < height:
                height = height * self.new_dimensions / width
                width = self.new_dimensions
            else:
                width = width * self.new_dimensions / height
                height = self.new_dimensions
            resized_img = image.resize((int(width), int(height)))
        elif type(self.new_dimensions) == tuple:
            resized_img = image.resize(self.new_dimensions)
        
        return resized_img

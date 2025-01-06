import numpy as np
import skimage

class Preprocessing:
    def __init__(self):
        pass

    def preprocess(self, image):
        image = self.minmaxNormalization(image)
        image = self.clahe(image)
        return image
        
    @staticmethod
    def minmaxNormalization(image):
        return (image - np.min(image)) / (np.max(image) - np.min(image))

    @staticmethod
    def clahe(image):
        # applies clahe to each axial slice of the image assuming the axis is [axial, coronal, sagittal]
        for i, axial_slice in enumerate(image):
            image[i] = skimage.exposure.equalize_adapthist(axial_slice)
        return image
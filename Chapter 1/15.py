from PIL import Image
from numpy import *
from scipy.ndimage import measurements,morphology

# load image and threshold to make sure it is binary
im = array(Image.open('convert3.png').convert('L'))
im = 1*(im<128)
labels, nbr_objects = measurements.label(im)
print("Number of objects:", nbr_objects)
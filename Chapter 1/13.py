from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('empire.jpeg').convert('L'))
im2 = filters.gaussian_filter(im,5)
im2 = Image.fromarray(uint8(im2))
im2.show()
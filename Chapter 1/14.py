from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('empire.jpeg'))
im2 = zeros(im.shape)
for i in range(3):
	im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = array(im2,'uint8')
im2 = Image.fromarray(uint8(im2))
im2.show()
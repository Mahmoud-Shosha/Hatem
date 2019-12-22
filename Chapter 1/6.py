from PIL import Image
from pylab import *


# read image to array
im = array(Image.open('empire.jpeg'))
# plot the image
imshow(im)
show()

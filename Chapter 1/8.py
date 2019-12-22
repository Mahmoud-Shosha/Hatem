from PIL import Image
from pylab import *


####### Image contours and histograms

# read image to array
im = array(Image.open('empire.jpeg').convert('L'))
# create a new figure
figure()
# don’t use colors
gray()
# show contours with origin upper left corner
contour(im, origin='image')
show()

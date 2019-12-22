from PIL import Image
from pylab import *


im = array(Image.open('empire.jpeg').convert('L'))
figure()
# hist() takes a one-dimensional array as input
# flatten() converts any array to a one-dimensional array
hist(im.flatten(), 1) # max 255 ==> specifies the number of bins to use
show()
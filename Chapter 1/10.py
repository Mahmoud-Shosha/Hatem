from PIL import Image
from pylab import *

# This plots an image and waits for the user to click three times in the image region of
# the figure window. The coordinates [x, y] of the clicks are saved in a list x.
im = array(Image.open('empire.jpeg'))
imshow(im)
print('Please click 3 points')
x = ginput(3)
print('you clicked:',x)
show()

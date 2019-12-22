from PIL import Image
from numpy import *


im = array(Image.open('empire.jpeg'))
print(im.shape, im.dtype) # shape ==> size (266, 189, 3), dtype ==> type uint8
im = array(Image.open('empire.jpeg').convert('L'),'f')
print(im.shape, im.dtype) # shape ==> size (266, 189), dtype ==> type float32

im = array(Image.open('empire.jpeg').convert('L'))
im1 = Image.fromarray(uint8(im))
im1.show()
im2 = 255 - im #invert the graylevels of the image
im2 = Image.fromarray(uint8(im2))
im2.show()
im3 = (100/255) * im + 100 #clamps the intensities to the interval 100 . . . 200
im3 = Image.fromarray(uint8(im3))
im3.show()
im4 = 255 * (im/255)**2 #squared ==> lowers the values of the darker pixels.
im4 = Image.fromarray(uint8(im4))
im4.show()

# # look in the book for page 23
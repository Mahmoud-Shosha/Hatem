from PIL import Image
from pylab import *
import rof

im = array(Image.open('empire.jpeg').convert('L'))
U,T = rof.denoise(im,im)
figure()
gray()
imshow(U)
axis('equal')
axis('off')
show()
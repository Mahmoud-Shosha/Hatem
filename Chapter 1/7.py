from PIL import Image
from pylab import *


im = array(Image.open('empire.jpeg'))
# plot the image
imshow(im)
# some points
x = [100,100,400,400]
y = [200,500,200,500]
# plot the points with red star-markers
plot(x,y,'r*')
# line plot connecting the first two points
plot(x[:2],y[:2])
# add title and show the plot
title('Plotting: "empire.jpg"')
# to remove the axix
# axis('off')
show()

# Notes
# plot(x,y) # default blue solid line
# plot(x,y,'r*') # red star-markers
# plot(x,y,'go-') # green line with circle-markers
# plot(x,y,'ks:') # black dotted line with square-markers
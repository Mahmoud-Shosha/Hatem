from PIL import Image


#  This method calculates an appropriate thumbnail size to preserve the aspect of the image
# Note that this function modifies the Image object in place
pil_im = Image.open('empire.jpeg')
pil_im.thumbnail((100, 100)) # shrink
pil_im.show()
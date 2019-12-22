from PIL import Image


pil_im = Image.open('empire.jpeg')

# Cropping a region from an image
# top-left then bottom-right ==> coordinates starts from top-left of image
box = (50,50,180,180)
region = pil_im.crop(box)
 # Rotating
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,(0,0,130,130))
# Resize (x, y)
out = pil_im.resize((500,800))
# Rotate (counter clockwise)
out = out.rotate(10)
out.show()
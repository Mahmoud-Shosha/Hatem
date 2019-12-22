from PIL import Image


# convert to grayscale
pil_im = Image.open('empire.jpeg') 
pil_im = pil_im.convert('L')
pil_im.show()

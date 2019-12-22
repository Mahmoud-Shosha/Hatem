import os
from PIL import Image


# Convert images to another format
filelist = ['convert1.jpeg', 'convert2.jpeg', 'convert3.png']
for infile in filelist:
	# PIL is smart enough to determine the image format from the file extension
	outfile = os.path.splitext(infile)[0] + '.jpg'
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print('Cannot convert '+infile)


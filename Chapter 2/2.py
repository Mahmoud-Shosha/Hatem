import sift
from PIL import Image
from numpy import *
from pylab import *
import os


imlist = ['convert1.jpeg', 'convert2.jpeg', 'convert3.png']
featlist = ['convert1.jpeg', 'convert2.jpeg', 'convert3.png']

nbr_images = len(imlist)
matchscores = zeros((nbr_images,nbr_images))
for i in range(nbr_images):
	for j in range(i,nbr_images): # only compute upper triangle
		print('comparing ', imlist[i], imlist[j])
		l1,d1 = sift.read_features_from_file(featlist[i])
		l2,d2 = sift.read_features_from_file(featlist[j])
		matches = sift.match_twosided(d1,d2)
		nbr_matches = sum(matches > 0)
		print('number of matches = ', nbr_matches)
		matchscores[i,j] = nbr_matches
# copy values
for i in range(nbr_images):
	for j in range(i+1,nbr_images): # no need to copy diagonal
		matchscores[j,i] = matchscores[i,j]
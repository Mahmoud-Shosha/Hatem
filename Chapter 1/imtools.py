# create a list of filenames of all images in a folder
import os
from PIL import Image
from numpy import *


# def get_imlist(path):
# 	""" Get the .jpeg images in the given path. """
# 	print([os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpeg')])

# get_imlist(os.getcwd())



# def imresize(im,sz):
# 	""" Resize an image array using PIL. """
# 	pil_im = Image.fromarray(uint8(im))
# 	return array(pil_im.resize(sz))

# im = array(Image.open('empire.jpeg'))
# im = imresize(im, (2000, 500))
# pil_im = Image.fromarray(uint8(im))
# pil_im.show()



# def histeq(im,nbr_bins=256):
# 	""" Histogram equalization of a grayscale image. """
# 	# get image histogram
# 	imhist,bins = histogram(im.flatten(),nbr_bins)
# 	cdf = imhist.cumsum() # cumulative distribution function
# 	cdf = 255 * cdf / cdf[-1] # normalize
# 	# use linear interpolation of cdf to find new pixel values
# 	im2 = interp(im.flatten(),bins[:-1],cdf)
# 	return im2.reshape(im.shape), cdf

# im = array(Image.open('empire.jpeg').convert('L'))
# im = histeq(im)[0]
# print(histeq(im)[1])
# pil_im = Image.fromarray(uint8(im))
# pil_im.show()



# def compute_average(imlist):
# 	""" Compute the average of a list of images. """
# 	# open first image and make into array of type float
# 	averageim = array(Image.open(imlist[0]), 'f')
# 	for imname in imlist[1:]:
# 		try:
# 			averageim += array(Image.open(imname))
# 		except:
# 			print(imname + '...skipped')
# 	averageim /= len(imlist)
# 	# return average as uint8
# 	return array(averageim, 'uint8')

# im = compute_average(['convert1.jpeg', 'convert2.jpeg', 'convert3.jpeg'])
# pil_im = Image.fromarray(uint8(im))
# pil_im.show()



def pca(X):
	""" Principal Component Analysis
	input: X, matrix with training data stored as flattened arrays in rows
	return: projection matrix (with important dimensions first), variance and mean.
	"""
	# get dimensions
	num_data,dim = X.shape
	# center data
	mean_X = X.mean(axis=0)
	X = X - mean_X
	if dim>num_data:
		# PCA - compact trick used
		M = dot(X,X.T) # covariance matrix
		e,EV = linalg.eigh(M) # eigenvalues and eigenvectors
		tmp = dot(X.T,EV).T # this is the compact trick
		V = tmp[::-1] # reverse since last eigenvectors are the ones we want
		S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
		for i in range(V.shape[1]):
			V[:,i] /= S
	else:
		# PCA - SVD used
		U,S,V = linalg.svd(X)
		V = V[:num_data] # only makes sense to return the first num_data
	# return the projection matrix, the variance and the mean
	return V,S,mean_X
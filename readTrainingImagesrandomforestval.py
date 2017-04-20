from PIL import Image
import os
import numpy as np
import pandas as pd
from random import randint

#Reads images from directory and creates the training set
def readImages(directory):
	features_train = []
	labels_train = []
	ident = np.identity(8)
	features_val = []
	labels_val = []

	i = 0
	#Directory to read the images from
	for im in os.listdir(directory):
		image = Image.open(directory+im)
		#Read label from image (label = first character of image name)
		label = int(im[0])
		label_one_hot = ident[label]
		#Read image pixels and store them as an array
		image_pixels = np.asarray(image.getdata()).reshape((image.size[1]*image.size[1]))
		if 0 == randint(0,5):
			#Add pixels as features to feature list
			features_val.append(image_pixels)
			#Add label to label list
			labels_val.append(label)
			i += 1
			continue
		#Add pixels as features to feature list
		features_train.append(image_pixels)
		#Add label to label list
		labels_train.append(label_one_hot)
		i += 1

	return features_train, labels_train, features_val, labels_val

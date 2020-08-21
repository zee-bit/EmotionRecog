#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:25:10 2020

@author: harit
"""

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from imutils import paths
import numpy as np
import os
import random

# preprocessing
# path to dataset
dataset = 'dataset-address'


# grab the list of images in our dataset directory, then initialize
# the list of data (i.e., images) and class images
print("[INFO] loading images...")
imagePaths = list(paths.list_images(dataset))
random.seed(42)
random.shuffle(imagePaths)
data = []
labels = []
# loop over the image paths
for imagePath in imagePaths:

	# extract the class label from the filename
	label = imagePath.split(os.path.sep)[-2]
	# load the input image (150x150) and preprocess it
	image = load_img(imagePath, target_size=(224, 224))
	image = img_to_array(image)/255.
	
 
	#image = preprocess_input(image)

	# update the data and labels lists, respectively
	data.append(image)
	labels.append(label)

# convert the data and labels to NumPy arrays
data = np.array(data, dtype="float32")
labels = np.array(labels)

# perform one-hot encoding on the labels
lb = LabelBinarizer()
labels = lb.fit_transform(labels)
label_value = to_categorical(labels)

# store data and labels in memory address
np.save('data address',data)
np.save('labels address',labels)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:37:33 2020

@author: harit
"""

# import the necessary packages
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from keras.models import Model
import matplotlib.pyplot as plt
from models import *
import numpy as np

# load preprocessed data and labels
data = np.load('data address')
labels = np.load('labels address')


# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.20, stratify=labels, random_state=42,shuffle = True)

# initialize data generators
aug_train = ImageDataGenerator(rescale= 1.0/255.,
	rotation_range=20,
	zoom_range=0.15,
	width_shift_range=0.2,
	height_shift_range=0.2,
	shear_range=0.15,
	horizontal_flip=True,
	fill_mode="nearest")

aug_test  = ImageDataGenerator(rescale= 1.0/255.)

# initialize batch size and epochs
BS = 32
EPOCHS = 50

# train model
hist = model.fit_generator(steps_per_epoch=len(trainX)//BS,
                           generator=aug_train.flow(trainX, trainY, batch_size=BS),
                           validation_data= (testX, testY),
                           validation_steps=len(testX)//BS,
                           epochs=EPOCHS)

# plotting training and testing graph
# print accuracy and loss graph
import matplotlib.pyplot as plt
plt.plot(hist.history["acc"])
plt.plot(hist.history['val_acc'])
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title("model accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(["Accuracy","Validation Accuracy","loss","Validation Loss"])
plt.show()

# storing model architecture for future use
model.save('model_name')

# printing confusion matrix
from sklearn.metrics import confusion_matrix
y_pred = model.predict(testX)
y_p = np.argmax(y_pred,axis=1)
y_true = np.argmax(testY,axis=1)
print(confusion_matrix(y_true,y_p))

# print classification report
from sklearn.metrics import classification_report
print(classification_report(y_true,y_p))


# increasing accuracy using cnn as feature extractor and svm as classifier
# creating train and test features for svm and xgboost
train_new = model_new.predict(trainX)
test_new = model_new.predict(testX)

# load and training svm
from sklearn.svm import SVC
svm = SVC(kernel='rbf')
svm.fit(train_new,np.argmax(trainY,axis=1))
svm_train = svm.score(train_new,np.argmax(trainY,axis=1))
print('training accuracy of svm: ',svm_train)
svm_score = svm.score(test_new,np.argmax(testY,axis=1))
print('testing accuracy of svm: ',svm_score)


# increasing accuracy using cnn as feature extractor and xgboost as boosting technics
from xgboost import XGBClassifier
xg = XGBClassifier()
xg.fit(train_new,np.argmax(trainY,axis=1))
xg_train = xg.score(train_new,np.argmax(trainY,axis=1))
print('training accuracy of xgboost: ',xg_train)
xg_score = svm.score(test_new,np.argmax(testY,axis=1))
print('testing accuracy of xgboost: ',xg_score)

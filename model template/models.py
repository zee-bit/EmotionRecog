#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:28:35 2020

@author: harit
"""


# importing libraries
from keras.layers import Dense , Dropout ,Flatten , MaxPooling2D
from keras.models import Model

# define model
# importing MobileNet_v2 for higher accuracy
from keras.applications import MobileNetV2
mobile = MobileNetV2(input_shape=(224,224,3),include_top=False,weights='imagenet')

#print(mobile.summary())

# layer should not be change
for layer in mobile.layers:
  layer.trainable = False


# Make output layer of mobilenet
op_layer = mobile.output
op_layer = MaxPooling2D(pool_size=(6,6))(op_layer)
op_layer = Flatten()(op_layer)
op_layer = Dense(128,activation='relu')(op_layer)
op_layer = Dropout((0.5))(op_layer)
op_layer = Dense(2,activation= 'softmax')(op_layer)

# Define model input and output
model = Model(inputs = mobile.input , outputs = op_layer)

# compiling model
model.compile(optimizer = 'adam', 
              loss = 'binary_crossentropy', 
              metrics = ['acc'])

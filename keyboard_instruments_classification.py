# -*- coding: utf-8 -*-

# import keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

classifier = Sequential()

classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3),
                             activation = 'relu'))
# 32 feature detectors with dimensions of 3x3
# also, a smaller input shape is good enough since we're running on CPU
# so, 2d array dimensions (64, 64) and 3 channels (RGB)
# we use this order because we use tensorflow backend, theano would
# have been 3, 64, 64

classifier.add(MaxPooling2D(pool_size = (2, 2)))
# this will reduce the size of feature maps, and divide by 2

classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Flatten())

classifier.add(Dense(units = 128, activation = 'relu'))

classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Having convolved, pooled, and flattened clasifier,
# time to compile our CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                   metrics = ['accuracy'])

# Fitting our CNN to the images
# Source: https://keras.io/preprocessing/image/
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=100,
        epochs=10,
        validation_data=test_set,
        validation_steps=50)

# Making new predictions

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('dataset/single_prediction/image_0099.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image) # should be piano
training_set.class_indices
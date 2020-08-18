import numpy as np

# Importing keras classes and functions using TensorFlow backend
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization, Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_accuracy

# Importing functions from different modules
from preprocess import preprocess_data
from utils import give_convolution_layer

# Defining constants
BATCH_SIZE = 128
EPOCHS = 30
IMG_SIZE = (48, 48)
# NUM_CLASSES = 7

X_train, X_test, y_train, y_test, NUM_CLASSES = preprocess_data(filename='/content/drive/My Drive/fer2013.csv',
                                                    image_size=IMG_SIZE) 

model = Sequential()

# 1st Convolution layer
model.add(give_convolution_layer(filters=64, kernel_size=(3,3),
            padding='same', use_bn=False, dropout_percentage=None, pool_size=(2,2)))

# 2nd Convolution layer
model.add(give_convolution_layer(filters=128, kernel_size=(3,3),
            padding='same', use_bn=True, dropout_percentage=0.3, pool_size=(2,2)))

# 3rd Convolution layer
model.add(give_convolution_layer(filters=256, kernel_size=(3,3),
            padding='same', use_bn=True, dropout_percentage=0.3, pool_size=(2,2)))

# 4th Convolution layer
model.add(give_convolution_layer(filters=512, kernel_size=(3,3),
            padding='same', use_bn=True, dropout_percentage=0.3, pool_size=(2,2)))

# 5th Convolution layer
model.add(give_convolution_layer(filters=1024, kernel_size=(3,3),
            padding='same', use_bn=True, dropout_percentage=0.3, pool_size=(2,2)))

# Flattening
model.add(Flatten())

# Fully connected layer 1st layer
model.add(Dense(512, activation='relu', kernel_initializer='glorot_normal'))
model.add(BatchNormalization())
model.add(Dropout(0.2))

# Last layer
model.add(Dense(NUM_CLASSES, activation='softmax', kernel_initializer='glorot_normal'))

# Compile model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=[categorical_accuracy])

# Print model summary
print(model.summary())

# Training the model
model.fit(X_train, y_train,
          BATCH_SIZE=BATCH_SIZE,
          EPOCHS=EPOCHS,
          verbose=1,
          validation_split=0.1111)

# Model will predict the probability values for 7 labels for a test image
test_output = model.predict(X_test)

new_X = np.argmax(test_output, axis=1)
y_test2 = np.argmax(test_output, axis=1)

# Calculating categorical accuracy taking label having highest probability
accuracy = [(x == y) for x, y in zip(new_X, y_test2)]
print("Accuracy on Test set : ", np.mean(accuracy))

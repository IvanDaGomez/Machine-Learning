import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
import numpy as np
import os
import random
# LOAD DATA
(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()


# (num_images, width, height, channels)
# (50000, 32, 32, 3)

# NORMALIZE PIXEL VALUES TO BE BETWEEN 0 AND 1
train_images, test_images = train_images / 255.0, test_images / 255.0
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                'dog', 'frog', 'horse', 'ship', 'truck']

# for i in range(9):
#     plt.subplot(330 + 1 + i)
#     plt.imshow(train_images[i])
#     plt.title(class_names[train_labels[i][0]])
# plt.show()

# CNN ARCHITECTURE
# A common architecture for a CNN is a stack of Conv2D and MaxPooling2D layers followed by a few densely connected layers.
# The idea is that the stack of convolutional and maxPooling layers extract the features from the image. Then these features are flattened and fed to densely connected layers that determine the class of an image
# The convolutional layers are used to find the features in the image. The maxPooling layers are used to reduce the dimensions of the image. The densely connected layers are used to determine the class of an image
# The final layer in a CNN is a densely connected layer with a softmax activation function with 10 nodes, which outputs a probability distribution over the 10 classes of images


model = keras.models.Sequential()


# INPUT SHAPE IS THE SHAPE OF THE IMAGE
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# SHRINKS THE IMAGE BY A FACTOR OF 2
model.add(keras.layers.MaxPooling2D((2, 2)))


model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
# SHRINKS THE IMAGE BY A FACTOR OF 2
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))

# THIS MODEL EXTRACTS FEATURES FROM THE IMAGE, AND THEN FLATTENS THE IMAGE TO BE FED INTO A DENSELY CONNECTED LAYER

# CLASSIFIER

# THIS LAYER FLATTENS THE IMAGE TO A VECTOR OF 1D
model.add(keras.layers.Flatten())

# DENSELY CONNECTED LAYER WITH 64 NODES, HIDDEN LAYER
model.add(keras.layers.Dense(64, activation='relu'))

# OUTPUT LAYER
model.add(keras.layers.Dense(10))


# TRAINING
model.compile(optimizer='adam', 
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
              metrics=['accuracy'])
print(train_images, train_labels)
# GET SAVED WEIGHTS
if os.path.exists('NN/weights/firstConvolutionalWeights.weights.h5'):
    model.load_weights('NN/weights/firstConvolutionalWeights.weights.h5')
else:
    history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels))
    # SAVE WEIGHTS
    model.save_weights('NN/weights/firstConvolutionalWeights.weights.h5')


# SHOW IMAGES
# predictions = model.predict(test_images)

# while True:
#     for i in range(9):
        
#         plt.subplot(330 + 1 + i) # location
#         i = random.randint(1, len(test_images))
#         plt.imshow(test_images[i]) #images
#         predictedIndex = np.argmax(predictions[i]) # distribution of values
#         plt.title(class_names[predictedIndex]) # labels

#     plt.show(block = True)

import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fasion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fasion_mnist.load_data()
# (number of images, pixels_width, pixels_height) grayscale

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# plt.figure()
# for image in train_images[:10]:
#     plt.imshow(image)

#     plt.colorbar()
#     plt.grid(False)
#     plt.show()

# Preprocessing
# squish values between 0 and 1

train_images = train_images / 255.0
test_images = test_images / 255.0

# The most basic neural network
model = keras.Sequential([
    # Input
    keras.layers.Flatten(input_shape = (28, 28)),
    # hidden normally smaller
    keras.layers.Dense(128, activation = 'relu'),
    # Output layer
    keras.layers.Dense(10, activation = 'softmax')
])

# Compile the model , arquitecture

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

# Training the model # watch for overfitting
model.fit(train_images, train_labels, epochs = 2)

# evaluation
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 1)

print('Test accuracy:', test_acc)

# Predictions

predictions = model.predict(test_images)
predictions = predictions[12]
index = np.argmax(predictions)
print(f'Class predicted: {class_names[index]}')

plt.figure()
plt.imshow(test_images[12])

plt.colorbar()

plt.grid(False)

plt.show()
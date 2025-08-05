# -*- coding: utf-8 -*-
import os

import tensorflow
tensorflow.__version__
import matplotlib.pyplot as plt
"""# My first generative AI model using fashion-mnist"""

from tensorflow.keras.datasets import fashion_mnist
import numpy as np
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

X_train.shape

def preprocess(arr):
  arr = arr.astype('float32') / 255.0
  arr = np.pad(arr, ((0,0), (2,2), (2,2)), constant_values = 0.0 )
  arr = np.expand_dims(arr, axis = -1)
  return arr

X_train = preprocess(X_train)
X_test = preprocess(X_test)
X_test.shape, X_train.shape

"""## Encoder"""

from tensorflow.keras import layers, models

encoder_input_layer = layers.Input(shape=X_train.shape[1:], name='encoder_input')
X = layers.Conv2D(32, (3, 3), activation='relu', strides=2, padding='same', name='enc_conv1')(encoder_input_layer)
X = layers.Conv2D(64, (3, 3), activation='relu', strides=2, padding='same', name='enc_conv2')(X)
X = layers.Conv2D(128, (3, 3), activation='relu', strides=2, padding='same', name='enc_conv3')(X)
shape_before_flatten = X.shape[1:]
print(shape_before_flatten)
X = layers.Flatten(name='enc_flatten')(X)
encoder_output = layers.Dense(30, name='encoder_output')(X)

encoder = models.Model(encoder_input_layer, encoder_output)

encoder.summary()

decoder_input_layer = layers.Input(shape=(30,), name='decoder_input')
X = layers.Dense(np.prod(shape_before_flatten), name='dec_dense')(decoder_input_layer)
X = layers.Reshape(shape_before_flatten, name='dec_reshape')(X)
X = layers.Conv2DTranspose(128, (3, 3), activation='relu', strides=2, padding='same', name='dec_conv1')(X)
X = layers.Conv2DTranspose(64, (3, 3), activation='relu', strides=2, padding='same', name='dec_conv2')(X)
X = layers.Conv2DTranspose(32, (3, 3), activation='relu', strides=2, padding='same', name='dec_conv3')(X)
decoder_output = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same', name='decoder_output')(X)
decoder = models.Model(decoder_input_layer, decoder_output)

decoder.summary()

autoencoder = models.Model(encoder_input_layer, decoder(encoder_output), name ='autoencoder')
autoencoder.summary()

"""## Train the encoder to reproduce the images"""

autoencoder.compile(optimizer = 'adam', loss = 'binary_crossentropy')



path = 'generativeAI/weights/firstGen.weights.h5'

# Ensure directory exists before saving
os.makedirs(os.path.dirname(path), exist_ok=True)
train = False
if os.path.exists(path) and not train:
    print("Loading existing weights...")
    autoencoder.load_weights(path)

else:
    print("Training model and saving weights...")
    autoencoder.fit(X_train, X_train, epochs = 20, batch_size = 128, shuffle = True, validation_data = (X_test, X_test))

    # SAVE WEIGHTS
    autoencoder.save_weights(path)
    print("Weights saved successfully.")

num_images = 20
indices = np.random.choice(len(X_test), num_images, replace=False)
selected_images = X_test[indices]
selected_labels = y_test[indices]  # Get corresponding labels

# Get predictions
preds = autoencoder.predict(selected_images)

plt.figure(figsize=(8,8))

plt.scatter(preds[:, 0], preds[:, 1], c='black', alpha=0.5, s=3)
plt.show()
# # Create figure with 3 rows: Original, Prediction, Label
# fig, axes = plt.subplots(nrows=3, ncols=num_images, figsize=(20, 6))

# # Plot images
# for i in range(num_images):
#     # Original Image
#     axes[0, i].imshow(selected_images[i].squeeze(), cmap='gray')
#     axes[0, i].set_title(f"Label: {selected_labels[i]}")
#     axes[0, i].axis('off')

#     # Reconstructed Image (Prediction)
#     axes[1, i].imshow(preds[i].squeeze(), cmap='gray')
#     axes[1, i].set_title("Prediction")
#     axes[1, i].axis('off')

#     # Difference (Error)
#     diff = np.abs(selected_images[i] - preds[i])
#     axes[2, i].imshow(diff.squeeze(), cmap='inferno')
#     axes[2, i].set_title("Difference")
#     axes[2, i].axis('off')

# # Adjust layout and show plot
# plt.tight_layout()
# plt.show()
mins, maxs = np.min(preds, axis=0), np.max(preds, axis=0)
sample = np.random.uniform(mins, maxs, size = (18, 2))
reconstructions = decoder.predict(sample)
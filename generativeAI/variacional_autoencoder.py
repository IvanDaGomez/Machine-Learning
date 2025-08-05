import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
import os
from tensorflow.keras.datasets import fashion_mnist

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

def preprocess(arr):
    arr = arr.astype('float32') / 255.0
    arr = np.pad(arr, ((0,0), (2,2), (2,2)), constant_values=0.0)
    arr = np.expand_dims(arr, axis=-1)
    return arr

X_train = preprocess(X_train)
X_test = preprocess(X_test)

class Sampling(layers.Layer):
    def call(self, inputs): 
        z_mean, z_log_var = inputs
        batch = tf.shape(z_mean)[0]
        dim = tf.shape(z_mean)[1]
        epsilon = tf.random.normal(shape=(batch, dim), mean=0.0, stddev=1.0)  # ✅ Fixed
        return z_mean + tf.exp(0.5 * z_log_var) * epsilon

# Encoder
encoder_input = layers.Input(shape=(32, 32, 1), name='encoder_input')
X = layers.Conv2D(32, (3, 3), strides=2, activation='relu', padding='same')(encoder_input)
X = layers.Conv2D(64, (3, 3), strides=2, activation='relu', padding='same')(X)
X = layers.Conv2D(128, (3, 3), strides=2, activation='relu', padding='same')(X)
shape_before_flattening = X.shape[1:]

X = layers.Flatten()(X)
z_mean = layers.Dense(2, name='z_mean')(X)
z_log_var = layers.Dense(2, name='z_log_var')(X)
z = Sampling()([z_mean, z_log_var])
encoder = models.Model(encoder_input, [z_mean, z_log_var, z], name='encoder')

# Decoder
decoder_input_layer = layers.Input(shape=(2,), name='decoder_input')  # ✅ Fixed shape
X = layers.Dense(np.prod(shape_before_flattening), name='dec_dense')(decoder_input_layer)
X = layers.Reshape(shape_before_flattening, name='dec_reshape')(X)
X = layers.Conv2DTranspose(128, (3, 3), activation='relu', strides=2, padding='same')(X)
X = layers.Conv2DTranspose(64, (3, 3), activation='relu', strides=2, padding='same')(X)
X = layers.Conv2DTranspose(32, (3, 3), activation='relu', strides=2, padding='same')(X)
decoder_output = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(X)
decoder = models.Model(decoder_input_layer, decoder_output)

# Variational Autoencoder (VAE)
class VAE(models.Model):
    def __init__(self, encoder, decoder, **kwargs):
        super().__init__(**kwargs)
        self.encoder = encoder
        self.decoder = decoder

    def train_step(self, data):
        with tf.GradientTape() as tape:
            z_mean, z_log_var, z = self.encoder(data)
            reconstruction = self.decoder(z)
            reconstruction_loss = tf.reduce_mean(tf.keras.losses.binary_crossentropy(data, reconstruction))
            kl_loss = tf.reduce_mean(
                tf.reduce_sum(
                    -0.5 * (1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var)),
                    axis=1  # ✅ Fixed KL Loss
                )
            )
            total_loss = reconstruction_loss + kl_loss

        grads = tape.gradient(total_loss, self.trainable_weights)
        self.optimizer.apply_gradients(zip(grads, self.trainable_weights))
        return {"loss": total_loss, "reconstruction_loss": reconstruction_loss, "kl_loss": kl_loss}

vae = VAE(encoder, decoder)
vae.compile(optimizer='adam')

# Saving Weights
path = 'generativeAI/weights/variacional_autoencoder.weights.h5'
if path and os.path.dirname(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

if os.path.exists(path):
    print("Loading existing weights...")
    vae.load_weights(path)
else:
    print("Training model...")
    vae.fit(X_train, X_train, epochs=20, batch_size=128, shuffle=True, validation_data=(X_test, X_test))
    vae.save_weights(path)
    print("Weights saved successfully.")

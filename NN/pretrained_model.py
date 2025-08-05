import os
import tensorflow as tf
import tensorflow_datasets as tfds

keras = tf.keras

# Load and split data
(raw_train, raw_validation, raw_test), metadata = tfds.load(
    'cats_vs_dogs',
    split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
    with_info=True,
    as_supervised=True
)

IMG_SIZE = 160
BATCH_SIZE = 32
SHUFFLE_BUFFER_SIZE = 1000

def format_example(image, label):
    image = tf.cast(image, tf.float32)
    image = (image / 127.5) - 1  # Normalize to [-1, 1]
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    return image, label

# Preprocess data
train = raw_train.map(format_example).shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
validation = raw_validation.map(format_example).batch(BATCH_SIZE)
test = raw_test.map(format_example).batch(BATCH_SIZE)

IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)
base_model = tf.keras.applications.MobileNetV2(
    input_shape=IMG_SHAPE,
    include_top=False,
    weights='imagenet'
)

base_model.trainable = False

# Add layers
global_average_layer = keras.layers.GlobalAveragePooling2D()
prediction_layer = keras.layers.Dense(1)

model = tf.keras.Sequential([
    base_model,
    global_average_layer,
    prediction_layer
])

base_learning_rate = 0.0001
model.compile(
    optimizer=keras.optimizers.RMSprop(learning_rate=base_learning_rate),
    loss=keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Train and evaluate
initial_epochs = 10
history = model.fit(
    train,
    epochs=initial_epochs,
    validation_data=validation
)

# Save the model
os.makedirs("NN/models", exist_ok=True)
model.save("NN/models/dogs_vs_cats.h5")

# for image, label in train.take(5):
#     plt.figure()
#     plt.imshow(image)
#     plt.title(get_label_name(label))
# plt.show()

import tensorflow as tf
import os
import numpy as np

path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

# with open(path_to_file) as file:
#     data = file.read()
#     print(f'length: {len(data)}')

# PREPROCESSING
text = ''
with open(path_to_file) as file:
    text = file.read()

vocab = sorted(set(text))


# Encoding and decoding dictionaries
char2idx = {element: index for index, element in enumerate(vocab)}
idx2char = {value : key for (key, value) in char2idx.items()}

# Optimized encoding function
def encode_text(text):
    return np.array([char2idx[char] for char in text])  # List comprehension for speed

# Optimized decoding function
def decode_text(integers):
    return ''.join([idx2char[integer] for integer in integers])  # Join for string output

text_as_int = encode_text(text)

seq_length = 100 # Length of sequence for a training example
examples_per_epoch = len(text)//(seq_length + 1)


# Create training examples / targets
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

# We need a 101 characters for every training example
# Drop the last characters if we can't put them into a batch
sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)

def split_input_target (chunk): # Example: hello
    input_text = chunk[:-1] # hell (removes the last element)
    target_text = chunk[1:] # ello (removes the first element)
    return input_text, target_text # hell, ello

# Apply the input_target function 
dataset = sequences.map(split_input_target)

# TRAINING BATCHES

BATCH_SIZE = 64
VOCAB_SIZE = len(vocab) # length of unique characters
EMBEDDING_DIM = 256
RNN_UNITS = 1024


# Buffer size to shuffle the dataset
# (TF data is designed to worl with possible infinite sequences,
# so it doesn't attempt to shuffle the entire sequence in memory. Instead,
# it maintains a buffer in which it shuffles elements).

BUFFER_SIZE = 10000

data = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder = True)

# def build_model (vocab_size, embedding_dim, rnn_units, batch_size):
#     model = tf.keras.Sequential([
#         tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                  
#                                   batch_input_shape = [batch_size, None]),
#         tf.keras.layers.LSTM(rnn_units,
#                              return_sequences = True,
#                              stateful = True,
#                              recurrent_initializer = 'glorot_uniform'),
#         tf.keras.layers.Dense(vocab_size)
#     ])
#     return model

def build_model(vocab_size, embedding_dim, rnn_units, batch_size, stateful=True):
    # Define model layers
    inputs = tf.keras.Input(batch_shape=(batch_size if stateful else None, None))
    embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)(inputs)
    lstm = tf.keras.layers.LSTM(
        rnn_units,
        return_sequences=True,
        stateful=stateful,
        recurrent_initializer='orthogonal',  # Default initializer
    )(embedding)
    outputs = tf.keras.layers.Dense(vocab_size)(lstm)

    # Build model
    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    return model
model = build_model(VOCAB_SIZE, EMBEDDING_DIM, RNN_UNITS, BATCH_SIZE)

# Pick a value based on probability (not always the higher value)

def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits = True)

model.compile(optimizer = 'adam', loss = loss)

# Creating checkpoints

checkpoint_dir = 'NN/text/training_checkpoints'

checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt:{epoch}" + ".weights.h5")

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath = checkpoint_prefix,
    save_weights_only = True
)
# history = model.fit(data, epochs = 80, callbacks = [checkpoint_callback])

# Rebuild the model with a batch size of 1
model = build_model(VOCAB_SIZE, EMBEDDING_DIM, RNN_UNITS, batch_size = 1)

# model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
latest_checkpoint = tf.train.latest_checkpoint(checkpoint_dir)
if latest_checkpoint:
    model.load_weights(latest_checkpoint)
else:
    print("No checkpoint found. Please ensure the checkpoint file exists.")
model.build(tf.TensorShape([1, None])) # we dont know the output

# Load any intermediate checkpoint

# checkpoint_num = 10
# model.load_weights(tf.train.load_checkpoint('NN/text/training_checkpoints/ckpt_' + str(checkpoint_num)))
# model.build(tf.TensorShape([1, None]))

# def generate_text(model, start_string):
#     # Evaluation step(generating text using the learned model)

#     # Number of characters to generate
#     num_generate = 800

#     # Converting our start string to numbers (vectorizing)
#     input_eval = encode_text(start_string) # Encoding
#     input_eval = tf.expand_dims(input_eval, 0) # Expand dimensions

#     # Empty string to store our results

#     text_generated = []

#     # Low temperatures results in more predictable text
#     # Higher temperatures results in more different text
#     # Experiment to find the best setting

#     temperature = 1.0

#     # here batch size == 1
#     model.reset_states()
#     for i in range(num_generate):
#         predictions = model(input_eval)
#         # remove the batch dimension
#         predictions = tf.squeeze(predictions, 0)

#         # using a categorical distribution to predict the character returned by the model
#         predictions = predictions / temperature
#         predicted_id = tf.random.categorical(predictions, num_samples=1).numpy() # Chooses a probability based on the distribution

#         # We pass the predicted character as the next input to the model
#         # along with the previous hidden state
#         input_eval = tf.expand_dims([predicted_id], 0)

#         text_generated.append(idx2char[predicted_id])
#     return (start_string + ''.join(text_generated))
def generate_text(model, start_string, num_generate=800, temperature=1.0):
    # Convert start string to numbers (vectorizing)
    input_eval = encode_text(start_string)  # Assume this function is defined elsewhere
    input_eval = tf.expand_dims(input_eval, 0)  # Expand dimensions for batch

    # Empty string to store results
    text_generated = []

    # Reset model states if required
    # model.reset_states()  

    for i in range(num_generate):
        predictions = model(input_eval)
        # Remove batch dimension
        predictions = tf.squeeze(predictions, 0)

        # Adjust predictions by temperature
        predictions = predictions / temperature

        # Sample the next character's index
        predicted_id = tf.random.categorical(predictions, num_samples=1).numpy()
        predicted_char = predicted_id[0][0]  # Extract scalar value

        # Pass the predicted character as next input
        input_eval = tf.expand_dims([predicted_char], 0)

        # Append the predicted character to the result
        text_generated.append(idx2char[predicted_char])  # Assume idx2char is defined

    return start_string + ''.join(text_generated)
# def generate_infinite_text(model, start_string):
#     # Evaluation step(generating text using the learned model)


#     # Converting our start string to numbers (vectorizing)
#     input_eval = encode_text(start_string) # Encoding
#     input_eval = tf.expand_dims(input_eval, 0) # Expand dimensions

#     # Empty string to store our results

#     # Low temperatures results in more predictable text
#     # Higher temperatures results in more different text
#     # Experiment to find the best setting

#     temperature = 1.0

#     # here batch size == 1
#     # model.reset_states()
#     while True:
#         predictions = model(input_eval)
#         # remove the batch dimension
#         predictions = tf.squeeze(predictions, 0)

#         # using a categorical distribution to predict the character returned by the model
#         predictions = predictions / temperature
#         predicted_id = tf.random.categorical(predictions, num_samples=1).numpy() # Chooses a probability based on the distribution

#         # We pass the predicted character as the next input to the model
#         # along with the previous hidden state
#         input_eval = tf.expand_dims([predicted_id], 0)

#         print(idx2char[predicted_id])
import tensorflow as tf

def generate_infinite_text(model, start_string, temperature=1.0):
    """
    Generates infinite text using the model and prints it continuously.
    Press Ctrl+C to stop the generation.
    """
    # Convert start string to numbers (vectorizing)
    input_eval = encode_text(start_string)  # Assume this function is defined elsewhere
    input_eval = tf.expand_dims(input_eval, 0)  # Expand dimensions for batch

    # Reset model states if required
    # model.reset_states()

    try:
        # Initialize a string to store the generated text
        generated_text = start_string
        while True:
            predictions = model(input_eval)
            # Remove batch dimension
            predictions = tf.squeeze(predictions, 0)

            # Adjust predictions by temperature
            predictions = predictions / temperature

            # Sample the next character's index
            predicted_id = tf.random.categorical(predictions, num_samples=1).numpy()
            predicted_char = predicted_id[0][0]  # Extract scalar value

            # Pass the predicted character as next input
            input_eval = tf.expand_dims([predicted_char], 0)

            # Convert the predicted ID to a character and append it to the result
            char = idx2char[predicted_char]  # Assume idx2char is defined
            generated_text += char

            # Print the generated text incrementally
            print(char, end='', flush=True)  # Print without new line and flush output
    except KeyboardInterrupt:
        print("\nText generation stopped.")

inp = input("Type a starting string: ")
generate_infinite_text(model, inp)
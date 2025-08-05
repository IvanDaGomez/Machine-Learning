import tensorflow as tf
from tensorflow import keras
import os
import numpy as np

VOCAB_SIZE = 88584
WORD_MAX_LEN = 250
BATCH_SIZE = 64
# Words already encoded into numbers
# Words are a list of number
# Labels are whether a sentence is positive or negative
(train_data, train_labels), (test_data,  test_labels) = keras.datasets.imdb.load_data(num_words = VOCAB_SIZE)

# We have to pass the data the same length, otherwise the model can't do the calculations

# Steps
# 1. If the review is greater than 250 words then trim off the extra words
# 2. If the review is less than 250 add the necessary amount of 0's to make it equal to 250
# There is a function in keras that does that

train_data = keras.preprocessing.sequence.pad_sequences(train_data, WORD_MAX_LEN)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, WORD_MAX_LEN)

# CREATING THE MODEL
print(train_data)
print(train_labels)
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(VOCAB_SIZE, 32), # Convert each word into a 32-dimension tensor
    tf.keras.layers.LSTM(32), # The Long Short Term Memory knows its 32 dimensions tensor
    tf.keras.layers.Dense(1, activation = 'sigmoid') # We want 1 value between 0 and 1 to know whether a word is positive or negative
])

model.compile(loss = 'binary_crossentropy',
              optimizer = 'rmsprop',
              metrics = ['acc'])


# GET SAVED WEIGHTS
path = 'NN/weights/firstRecurrentWeights.weights.h5'
if os.path.exists(path):
    model.build((None, WORD_MAX_LEN))
    model.load_weights(path)
else:
    history = model.fit(train_data, train_labels, epochs = 10, validation_split = 0.2)

    # SAVE WEIGHTS
    model.save_weights(path)

# results = model.evaluate(test_data, test_labels)

# print(results)

# MAKING PREDICTIONS

word_index = keras.datasets.imdb.get_word_index()

def encode_text (text):
    tokens = keras.preprocessing.text.text_to_word_sequence(text) # Splits the word into list (removes uppercase)
    tokens = [word_index[word] if word in word_index else 0 for word in tokens] # If the word exists in the vocabulary include it else don't count it 
    return keras.preprocessing.sequence.pad_sequences([tokens], WORD_MAX_LEN)[0]

# Decode function

# Reverses the dictionary
reverse_word_index = {value : key for (key, value) in word_index.items()}

def decode_integers(integers):
    PAD = 0
    text = ''
    for integer in integers:
        if integer != PAD: # Remove 0's which are not important 
            text += reverse_word_index[integer] + ' ' # Creating the whole word based on the revsersed dictionary
    return text.strip() # Without spaces


# Now predict

def predict(arr):
    if isinstance(arr, str):
        arr = [arr]
    encoded_text = [encode_text(text) for text in arr]
    pred = np.zeros((len(arr), WORD_MAX_LEN))
    for i in range(len(arr)):
        pred[i] = encoded_text[i]
    result = model.predict(pred)
    return result
positive_review_1 = "That movie was so awesome! I really loved it and would watch it again because it was amazingly great."
positive_review_2 = "What an incredible movie! The story was captivating, and the acting was top-notch. I’d absolutely recommend it to anyone."
positive_review_3 = "I had such a great time watching that movie. The visuals were stunning, and the soundtrack was unforgettable."

negative_review_1 = "That movie sucked. I hated it and wouldn't watch it again. Was one of the worst things I've ever watched."
negative_review_2 = "I couldn’t get into that movie at all. It was boring, poorly made, and a complete waste of time."
negative_review_3 = "The plot made no sense, and the characters were flat. I wouldn’t recommend it to anyone."

neutral_review_1 = "It was an okay movie. Some parts were entertaining, but others dragged on. I wouldn’t go out of my way to watch it again, but it wasn’t the worst either."

text_array = [positive_review_1,
positive_review_2,
positive_review_3,
negative_review_1,
negative_review_2,
negative_review_3,
neutral_review_1]
predictions = predict(text_array)

for i in range(len(predictions)):
        
    sentiment = 'neutral' # negative
    if predictions[i][0] > 0.6:
        sentiment = 'positive'
    elif predictions[i][0] < 0.4:
        sentiment = 'negative'

    print(f'Sentiment: {sentiment} {predictions[i][0]}\n{text_array[i]}')
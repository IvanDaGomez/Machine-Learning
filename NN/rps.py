# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import tensorflow as tf
import numpy as np
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    class_names = {'R': 1, 'P': 2, 'S': 3}
    reversed_class_names = {value: key for key, value in class_names.items()}
    max_opponent_history_to_look = 10 # 10 last movements to look

    # Encode plays
    encoded_history = [class_names.get(play, 0) for play in opponent_history[-max_opponent_history_to_look:]]
    # Pad the array to ensure it has exactly 10 elements
    encoded_history = np.pad(encoded_history, (max_opponent_history_to_look - len(encoded_history), 0), 'constant')
    encoded_history = np.expand_dims(encoded_history, axis=0)
    # Model
    model = tf.keras.Sequential([
        # First layer should be the prev play and the history
        tf.keras.layers.Dense(max_opponent_history_to_look),
        # Middle layer will be a dense layer with 256 options
        tf.keras.layers.Dense(256),
    
        tf.keras.layers.Dense(64),
        # Last layer should be a 3 neuron with a probability distribution
        tf.keras.layers.Dense(3, activation='sigmoid')
    ])

    guess = model.predict(encoded_history)

    idx = np.argmax(guess[0])

    return reversed_class_names[idx]
print(player('R', opponent_history = ['R', 'R', 'R', 'R', 'P']))
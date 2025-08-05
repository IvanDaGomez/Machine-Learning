import gym
import time
import matplotlib.pyplot as plt
import numpy as np
# Create the environment
env = gym.make('FrozenLake-v1')  # Use 'human' render mode for visualization

STATES = env.observation_space.n
ACTIONS = env.action_space.n
Q = np.zeros((STATES, ACTIONS))

state = env.observation_space.sample()
observation = env.reset()




EPISODES = 200000 # how many times to run the environment from the beginning
MAX_STEPS = 100 # max number of steps allowed for each run of environment
LEARNING_RATE = 0.81 # the higher the faster it learns
GAMMA = 0.96
RENDER = True
epsilon = 0.9 # Start with a 90% chance of picking a random action

rewards = []
for episode in range(EPISODES):

    state = env.reset()
    for _ in range(MAX_STEPS):
        if RENDER and episode >= EPISODES - 5:
            img = env.render(mode='rgb_array')  # Render the current state
            plt.imshow(img)
            plt.axis(False)
            plt.draw()
            plt.pause(0.000001)  # Pause to update the plot
        if np.random.uniform(0, 1) < epsilon: # Check if a randomly selected value is less than epsilon.
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        next_state, reward, done, _ = env.step(action)

        Q[state, action] = Q[state, action] + LEARNING_RATE * (reward + GAMMA * np.max(Q[next_state, :]) - Q[state, action])

        state = next_state
        if done:
            rewards.append(reward)
            epsilon -= 0.0001
            print(f'{episode}.reward:', reward)
            break

print(Q)
print(f'Average reward: {sum(rewards)/len(rewards)}')

# code to pick action





# # Loop to play the game
# while True:
#     img = env.render(mode='rgb_array')  # Render the current state
#     plt.imshow(img)
#     plt.axis(False)
#     plt.draw()
#     plt.pause(0.2)  # Pause to update the plot
#     action = env.action_space.sample()  # Select a random action
#     new_state, reward, done, info = env.step(action)  # Perform the action

#     if done:  # Check if the episode is over
#         print(f"Game over. Reward: {reward}")
#         continue  # Exit the loop

# plt.close()  # Close the plot after the loop ends

# # Close the environment when done
# env.close()

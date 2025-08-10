# import necessary libraries
import numpy as np
import random

# Environment setup
road_length = 5 # the road will have 5 position 0, 4, our is to reach position 4
actions = ['left', 'right'] # agent can take left or right


#Q-table initiatialisation
Q = np.zeros((road_length, len(actions))) 

#Hyperparameters
episodes = 1000 # number of training interation, leads to better learning rates
learning_rate = 0.8 #Helps the agent to adapt quickly
gamma = 0.9 #it will have a high rewards
epsilon = 0.3 # helps the agent to discover paths

for episode in range(episodes):
    state = 0 # start position 0

    while state != 4: # goal is position 4
         if random.uniform(0,1) < epsilon:
              actions = random.randint(0,1) # Explore my random action

         else: 
            action = np.argmax(Q[state])
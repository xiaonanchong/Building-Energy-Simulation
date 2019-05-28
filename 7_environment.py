
# coding: utf-8

# explore the energyplus simultion environment

# In[2]:

import gym
env_id2 = 'gym_energyplus:EnergyPlus-v0'
env = gym.make(env_id2)
print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.high)
print(env.action_space.low)


# In[3]:

import numpy as np

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.rcParams['figure.figsize'] = [15, 5]
plt.title('random sampled actions at each timestep')
plt.xlabel('time step')

observation = env.reset()
for i in range(800):
    action =  env.action_space.sample() #np.asarray([20, 20, 1.75, 1.75])
    observation, reward, done, info = env.step(action)
    if i == 0:        
        plt.plot(i, observation[1], 'bo', label='west zone temperature')
        plt.plot(i, observation[0], 'go', label='outdoor temperature')
        plt.plot(i, reward, 'y^', label='reward')
    else:
        plt.plot(i, reward, 'y^')
        plt.plot(i, observation[1], 'bo')
        plt.plot(i, observation[0], 'go')
plt.legend()


# In[ ]:




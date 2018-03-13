#!/usr/bin/env python3

import time
import sys
import argparse

import numpy as np
import gym
import gym_duckietown

from supervised.autoenc_angle import Model

parser = argparse.ArgumentParser()
parser.add_argument('--env-name', default='Duckie-SimpleSim-v0')
args = parser.parse_args()

env = gym.make(args.env_name)
obs = env.reset()
env.render()

model = Model()
model.load('trained_models/angle_model.pt')

#Define the gains
kp = 0.01

try:
    while True:
        angle = model.getAngle(obs)
        print('angle=%.2f' % angle)
        
        vel = np.array([0.6+kp*angel, 0.6-kp*angle])

        obs, reward, done, info = env.step(vel)
        #print('stepCount = %s, reward=%.3f' % (env.stepCount, reward))

        env.render()

        if done:
            print('done!')
            env.reset()
            env.render()

        time.sleep(0.1)

except Exception as e:
    print(e)
    env.close()
    time.sleep(0.25)

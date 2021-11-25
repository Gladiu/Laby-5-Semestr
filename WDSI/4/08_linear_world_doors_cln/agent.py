# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, walls, doors, loc, dir, eps_move, eps_perc_true, eps_perc_false):
        self.size = size
        self.walls = walls
        self.doors = doors
        self.eps_move = eps_move
        self.eps_perc_true = eps_perc_true
        self.eps_perc_false = eps_perc_false
        # list of valid locations
        self.locations = list({*locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.action_dir = -1

        self.t = 0
        self.P = 1.0 / self.size * np.ones(self.size, dtype=np.float)

    def __call__(self):
        # change direction after 20 steps
        if self.t % 20 == 0:
            self.action_dir *= -1

        # move by one or two cells
        action = self.action_dir * np.random.choice([1, 2])

        # use information about requested action to update posterior
        # TODO PUT YOUR CODE HERE
        self.predict_posterior(action)

        # ------------------

        self.t += 1

        return action

    def predict_posterior(self, action):
        # predict posterior using requested action
        # TODO PUT YOUR CODE HERE
        
        for i in range(len(self.P)):
            for j in [-2, -1, 0, 1, 2]:
                probalility = 0
                if abs(j) == 0:
                    probalility = 1- 6*self.eps_move
                if abs(j) == 1:
                    probalility = 2*self.eps_move
                if abs(j) == 2:
                    probalility = self.eps_move
                index = i+j+action
                if index >= len(self.P-1):
                    index = index - len(self.P-1)
                self.P[index] = probalility + self.P[index]

        for i in range(len(self.P)):
            self.P[i] = self.P[i]/np.amax(self.P)
        # ------------------
        return 

    def correct_posterior(self, percept):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE
        probability = 0
        for i in range(len(self.P)):
            index = i
            if index >= len(self.P-1):
                index = index - len(self.P-1)
            if percept and index in self.doors:
                probability = 1 - self.eps_perc_true
            if percept == False and index in self.doors:
                probability = self.eps_perc_true
            if (percept == False) and ((index in self.doors) == False):
                probability = 1 - self.eps_perc_false
            if percept and ((index in self.doors) == False):
                probability = self.eps_perc_false
            self.P[index] = probability + self.P[index]
        
        for i in range(len(self.P)):
            self.P[i] = self.P[i]/amax(self.P)
        return
        # ------------------

    def get_posterior(self):
        print(self.P)
        return self.P

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



        # ------------------

        self.t += 1

        return action

    def predict_posterior(self, action):
        # predict posterior using requested action
        # TODO PUT YOUR CODE HERE
        
        self.P = np.zeros(len(self.P))
        for i in range(len(self.P)):
            for j in [-2, -1, 0, 1, 2]:
                if abs(j) == 0:

                if abs(j) == 1:
                if abs(j) == 2:
            self.P[i+j] = 
            

        # ------------------

        #return

    def correct_posterior(self, percept):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE

        return
        # ------------------

    def get_posterior(self):
        return self.P

# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, walls, loc, dir, sigma_move, sigma_perc):
        self.size = size
        self.walls = walls
        self.sigma_sq_move = sigma_move ** 2
        self.sigma_sq_perc = sigma_perc ** 2
        # list of valid locations
        self.locations = list({*locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.action_dir = -1

        self.t = 0
        self.n = 20
        # initial particle set
        self.p = np.random.random(self.n) * self.size
        self.w = np.ones(self.n, dtype=float) / self.n

    def __call__(self):
        # if reached one of the ends then start moving in the opposite direction
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
        for i in range(len(self.p)):
            self.p[i] += action + np.random.normal(0, self.sigma_sq_move, 1)[0]
        # ------------------

        return

    def calculate_weights(self, percept):
        for i in range(len(self.p)):
            self.w *= np.random.normal((percept-self.p[i]), self.sigma_sq_perc, 1)[0]
        # TODO PUT YOUR CODE HERE

    def correct_posterior(self):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE

        pass
        # ------------------

    def get_particles(self):
        return self.p

    def get_weights(self):
        return self.w

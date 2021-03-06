# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, walls, loc, dir, sigma_move, sigma_perc, dt):
        self.size = size
        self.walls = walls
        # list of valid locations
        self.locations = list({*locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.dt = dt
        self.action_dir = 1

        self.sigma_perc = sigma_perc
        self.sigma_move = sigma_move

        self.t = 0

        # create matrices used in Kalman filter
        # TODO PUT YOUR CODE HERE
        self.mu = np.array([[0],[0]])
        self.Sigma = np.array([[1, 0],[0, 10]])


        # ------------------

    def __call__(self):
        # use information about requested action to update posterior
        # TODO PUT YOUR CODE HERE
        self.predict_posterior()

        # ------------------

        # this function does not return anything
        return

    def predict_posterior(self):
        # predict posterior
        # TODO PUT YOUR CODE HERE
        Q = np.array([[0.25*self.dt ** 4, 0.5 * self.dt ** 3], [0.5 * self.dt ** 3, self.dt ** 2]]) * self.sigma_move**2

        F = np.array([[1, self.dt], [0, 1]])
        
        self.mu = F @ self.mu
        self.Sigma = F @ self.Sigma @ F.T + Q

        # ------------------

        # this function does not return anything
        return

    def correct_posterior(self, percept):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE
        H = np.array([[1, 0]])
        R = self.sigma_perc ** 2
        y = percept - H @ self.mu

        K = self.Sigma @ H.T @ np.linalg.inv(H @ self.Sigma @ np.transpose(H) + R)
        self.mu = self.mu + K @ y
        self.Sigma = (np.eye(2) - K @ H) @ self.Sigma

        # ------------------

        # this function does not return anything
        return

    def get_posterior(self):
        return self.mu, self.Sigma

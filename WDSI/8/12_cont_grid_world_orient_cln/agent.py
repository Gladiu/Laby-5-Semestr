# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, landmarks, sigma_move_fwd, sigma_move_turn, sigma_perc):
        self.size = size
        self.landmarks = landmarks
        self.sigma_move_fwd = sigma_move_fwd
        self.sigma_move_turn = sigma_move_turn
        self.sigma_perc = sigma_perc
        self.t = 0
        self.n = 500
        # create an initial particle set as 2-D numpy array with size (self.n, 3) (self.p)
        # and initial weights as 1-D numpy array (self.w)
        # TODO PUT YOUR CODE HERE
        self.p = np.ones(shape=(self.n, 3))
        for i in range(self.n):
                self.p[i][0] = random.random() * size
                self.p[i][1] = random.random() * size
                self.p[i][2] = random.random() * math.pi/2.0

        self.w = np.ones(shape=(self.n))/self.n
        # ------------------

    def __call__(self):
        # turn by -pi/20.0 and move forward by 1
        action = (-math.pi/20, 1.0)
        # no turn, only move forward by 1.0
        # action = (0.0, 1.0)

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
            self.p[i][2] += action[0] + np.random.normal(0, self.sigma_move_turn ** 2, 1)%math.pi/2.0
            self.p[i][0] += (action[1]+np.random.normal(0, self.sigma_move_fwd , 1))*np.sin(self.p[i][2])
            self.p[i][1] += (action[1]+np.random.normal(0, self.sigma_move_fwd  , 1))*np.cos(self.p[i][2])

        # ------------------

        # this function does not return anything
        return

    def calculate_weights(self, percept):
        # calculate weights using percept
        # TODO PUT YOUR CODE HERE
        for i in range(len(self.p)):
            self.w[i] = 1
            for j in range(len(self.landmarks)):
                distance_till_landmark = np.sqrt((self.p[i][0]-self.landmarks[j][0]) ** 2 + (self.p[i][1]-self.landmarks[j][1]) ** 2)

                self.w[i] *= (math.exp(-((distance_till_landmark-percept[j]) ** 2)/ self.sigma_perc))
        
        # normalizacja
        sumw = sum(self.w)
        for i in range(len(self.p)):
            self.w[i] /= sumw
        # ------------------
        # this function does not return anything
        return

    def correct_posterior(self):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE
        if True:
            rng = np.random.default_rng()
            # zbiór nowych cząsteczek
            new_p = []
            # początkowy indeks (miejsce skąd zaczynamy)
            M = len(self.p)
            index = rng.integers(0, M)
            # "beta" będzie oznaczała jak daleko znajduje się strzałka od początku cząsteczki o indeksie "index"
            beta = 0.0
            # największa waga cząsteczki, żeby wybrać sensowny zakres losowanych wartości "beta"
            mw = max(self.w)
            # losujemy M cząsteczek
            for i in range(M):
                # przesuwamy się o "beta" z rozkładu jednostajnego od 0 do 2mw
                beta += np.random.uniform(0, 2.0*mw, 1)[0]
                # szukamy indeksu, który odpowiada aktualnemu położeniu strzałki
                while beta > self.w[index]:
                    # przeskakujemy na następną cząsteczkę, odejmując jej wagę od "beta"
                    beta -= self.w[index]
                    index = (index+1) % M
                # dodaj cząsteczkę o indeksie "index" do zbioru wylosowanych cząsteczek
                new_p.append(self.p[index])
            # ------------------
            self.p = np.ones(shape=(len(new_p), 3))
            for i in range(len(new_p)):
                self.p[i] = (new_p[i])
        # ------------------
        # this function does not return anything
        return

    def get_particles(self):
        return self.p

    def get_weights(self):
        return self.w

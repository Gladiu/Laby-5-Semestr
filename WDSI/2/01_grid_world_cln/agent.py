# prob.py
# This is

import random
import numpy as np
import queue

from gridutil import *


class Agent:
    def __init__(self, size, walls, loc, dir, goal):
        self.size = size
        self.walls = walls
        # list of valid locations
        self.locations = list({*locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.goal = goal

        self.t = 0
        self.path = self.find_path()

    def __call__(self):
        action = 'N'

        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE



        # ------------------

        return action

    def find_path(self):
        path = []
        if False:
            nodes = {
                    (1, 6):[(1, 7)],
                    (1, 7):[(2, 7)],
                    (2, 7):[(1, 7), (2, 8), (3, 7)],
                    (2, 8):[(2, 9), (2, 7), (3, 8)],
                    (3, 7):[(2, 7), (3, 6), (3, 8)],
                    (3, 8):[(2, 8), (3, 7), (3, 9)],
                    (3, 6):[(3, 7)],
                    (2, 9):[(2, 8), (3, 9)]
                    }
        # find path from sel.loc to self.goal
        # TODO PUT YOUR CODE HERE
        nodes= {}
        for x in range(self.size):
            for y in range(self.size):
                nodes[(x, y)] = []
                if  ((x - 1, y ) not in self.walls) and x-1 >= 0:
                    nodes[(x,y)].append((x - 1, y))
                if  ((x + 1, y ) not in self.walls):
                    nodes[(x,y)].append((x + 1, y))
                if  ((x, y + 1 ) not in self.walls):
                    nodes[(x,y)].append((x, y + 1))
                if  ((x, y - 1 ) not in self.walls) and y-1 >= 0:
                    nodes[(x,y)].append((x, y - 1))
        for key in list(nodes):
            if len(nodes[key]) ==  0:
                del nodes[key]
        print(nodes)

        # s - wierzchołek startowy
        # g - wierzchołek docelowy
        # nodes - lista wierzchołków
        s = self.loc
        g = self.goal


        # lista odwiedzonych wierzchołków
        visited = set()
        # słownik poprzedników
        #parent = {n: None for n in nodes}
        parent = {}

        q = queue.Queue()

        # dodaj wierzchołek startowy
        q.put(s)
        # ustaw jego poprzednika jako jego samego, aby oznaczyć go jako odwiedzony
        parent[s] = s
        # dopóki kolejka nie jest pusta, czyli są jeszcze jakieś wierzchołki do odwiedzenia
        while not q.empty():
            # pobierz następny wierzchołek i usuń go z kolejki
            cur_n = q.get()
            # przerwij jeśli dotarliśmy do celu
            if cur_n == g:
                break

            # dla wszystkich krawędzi z aktualnego wierzchołka
            for nh in nodes[cur_n]:
                # jeśli sąsiad nie był jeszcze odwiedzony
                if nh not in visited:
                    # oznacz jako odwiedzony i dodaj do kolejki
                    parent[nh] = cur_n
                    visited.add( nh)
                    q.put(nh)


        # zaczynamy od wierzchołka docelowego i cofamy się po znalezionej ścieżce
        cur_n = g
        # dopóki nie dotrzemy do startu
        while cur_n != s:
          # dodajemy aktualny wierzchołek i przechodzimy do poprzednika
            path.append( cur_n)
            print(cur_n)
            cur_n = parent[cur_n]
        # wierzchołki są w odwrotnej kolejności, więc odwracamy listę
        path.append(s)
        path.reverse()
                

            # ------------------

        return path

    def get_path(self):
        return self.path

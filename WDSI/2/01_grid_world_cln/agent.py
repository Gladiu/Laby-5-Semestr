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
        current_tile = self.path[self.t]
        next_tile = self.path[self.t+1]
        return_value = 0
        if int(current_tile[0] - next_tile[0]) == -1:
            return_value = 'E'
        if int(current_tile[0] - next_tile[0]) == 1:
            return_value ='W'
        if int(current_tile[1] - next_tile[1]) == -1:
            return_value = 'N'
        if int(current_tile[1] - next_tile[1]) == 1:
            return_value = 'S'
        self.t = self.t + 1
        return return_value

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
                if  ((x + 1, y ) not in self.walls) and x+1 < 16:
                    nodes[(x,y)].append((x + 1, y))
                if  ((x, y + 1 ) not in self.walls) and y+1 < 16:
                    nodes[(x,y)].append((x, y + 1))
                if  ((x, y - 1 ) not in self.walls) and y-1 >= 0:
                    nodes[(x,y)].append((x, y - 1))

        # s - wierzcho??ek startowy
        # g - wierzcho??ek docelowy
        # nodes - lista wierzcho??k??w
        s = self.loc
        g = self.goal


        # lista odwiedzonych wierzcho??k??w
        visited = set()
        # s??ownik poprzednik??w
        #parent = {n: None for n in nodes}
        parent = {}

        q = queue.Queue()

        # dodaj wierzcho??ek startowy
        q.put(s)
        # ustaw jego poprzednika jako jego samego, aby oznaczy?? go jako odwiedzony
        parent[s] = s
        # dop??ki kolejka nie jest pusta, czyli s?? jeszcze jakie?? wierzcho??ki do odwiedzenia
        while not q.empty():
            # pobierz nast??pny wierzcho??ek i usu?? go z kolejki
            cur_n = q.get()
            # przerwij je??li dotarli??my do celu
            if cur_n == g:
                break

            # dla wszystkich kraw??dzi z aktualnego wierzcho??ka
            for nh in nodes[cur_n]:
                # je??li s??siad nie by?? jeszcze odwiedzony
                if nh not in visited:
                    # oznacz jako odwiedzony i dodaj do kolejki
                    parent[nh] = cur_n
                    visited.add( nh)
                    q.put(nh)


        # zaczynamy od wierzcho??ka docelowego i cofamy si?? po znalezionej ??cie??ce
        cur_n = g
        # dop??ki nie dotrzemy do startu
        while cur_n != s:
          # dodajemy aktualny wierzcho??ek i przechodzimy do poprzednika
            path.append( cur_n)
            print(cur_n)
            cur_n = parent[cur_n]
        # wierzcho??ki s?? w odwrotnej kolejno??ci, wi??c odwracamy list??
        path.append(s)
        path.reverse()
                

            # ------------------

        return path

    def get_path(self):
        return self.path

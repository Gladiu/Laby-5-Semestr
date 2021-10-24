# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *

def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

class Agent:
    def __init__(self, size, walls, graph, loc, dir, goal):
        self.size = size
        self.walls = walls
        self.graph = graph
        # list of valid locations
        self.locations = list(self.graph.keys())
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.goal = goal

        self.t = 0
        self.path = self.find_path()

    def __call__(self, t):
        action = self.loc

        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE
        action = self.path[t]


        # ------------------

        return action

    def find_path(self):
        path = []

        # find path from sel.loc to self.goal
        # TODO PUT YOUR CODE HERE

        # s - wierzchołek startowy
        # g - wierzchołek docelowy
        # nodes - lista wierzchołków
        # najpierw jest numer wierzchołka, a potem jest koszt
        nodes =  self.graph
        s = self.loc
        g = self.goal
        # zbiór wierzchołków odwiedzonych
        visited = set()
        # słownik kosztów
        cost = {n: math.inf for n in nodes}
        # słownik poprzedników
        parent = {n: None for n in nodes}
        # utwórz kolejke, w której elementy są ułożone nie w kolejności wprowadzania, lecz w kolejności priorytetu.
        q = queue.PriorityQueue()
        # dodaj wierzchołek startowy
        q.put(s)
        cost[s] = 0
        # dopóki kolejka nie jest pusta, czyli są jeszcze jakieś wierzchołki do odwiedzenia
        while not q.empty():
            # pobierz wierzchołek o najmniejszym priotytecie i usuń go z kolejki
            cur_n = q.get()
            # przerwij jeśli odwiedzony
            if cur_n in visited:
              continue
            # dodaj wierzchołek do listy odwiedonych
            visited.add(cur_n)
            # przerwij jeśli dotarliśmy do celu
            if cur_n == g:
                break
            # dla wszystkich krawędzi z aktualnego wierzchołka    
            for nh in nodes[cur_n]:
                # przerwij jeśli sąsiad był już odwiedzony
                if nh in visited: 
                    continue  
                # pobierz koszt sąsiada lub przypisz mu inf
                old_cost = cost[nh]
                # oblicz koszt dla danego wierzchołka 
                distance = calc_distance(cur_n[0], cur_n[1], nh[0], nh[1])
                new_cost = cost[cur_n] + distance
               # rozważ nową ścieżkę tylko wtedy, gdy jest lepsza niż dotychczas najlepsze ścieżka
                if new_cost < old_cost:
                    # zaktualizuj wartość sąsiada w słowniku kosztów
                    cost[nh] = new_cost
                    # ustaw poprzednika
                    parent[nh] = cur_n
                    # dodaj sąsiada do kolejki
                    q.put(nh)
        # odtwórz ścieżkę
        cur_n = g
        while cur_n is not None:
            path.append(cur_n)
            cur_n = parent[cur_n]
        path.reverse()



        

        # ------------------

        return path

    def get_path(self):
        return self.path

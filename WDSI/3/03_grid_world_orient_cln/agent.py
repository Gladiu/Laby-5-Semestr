# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *

def calc_cost(dir, x1, y1, x2, y2):
    cur_dir = []
    if dir == 'W':
        cur_dir = np.array([[1], [0]])
    if dir == 'E':
        cur_dir = np.array([[-1], [0]])
    if dir == 'S':
        cur_dir = np.array([[0], [-1]])
    if dir == 'N':
        cur_dir = np.array([[0], [1]])
    next_dir = np.array([[x2 - x1], [y2 - y1]])
    actioncost = 1.0
    turnright = (np.array([[0, 1],[-1, 0]]) @ cur_dir) == next_dir
    turnleft =  np.array([[0, -1], [1, 0]]) @ cur_dir == next_dir
    if turnright.all():
        actioncost = 2.0
    if turnleft.all():
        actioncost = 5.0
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)) + actioncost

def calc_movement(dir, x1, y1, x2, y2):
    cur_dir = []
    if dir == 'W':
        cur_dir = np.array([[-1], [0]])
    if dir == 'E':
        cur_dir = np.array([[1], [0]])
    if dir == 'N':
        cur_dir = np.array([[0], [1]])
    if dir == 'S':
        cur_dir = np.array([[0], [-1]])
    next_dir = np.array([[x2 - x1], [y2 - y1]])
    print('------------')
    print(cur_dir)
    print(next_dir)
    action = 'forward'
    turnright = (np.array([[0, 1],[-1, 0]]) @ cur_dir) == next_dir
    turnleft =  (np.array([[0, -1],[1, 0]]) @ cur_dir) == next_dir
    turnaround = (np.array([[0, -1],[1, 0]]) @ np.array([[0, -1],[1, 0]]) @ cur_dir) == next_dir
    if turnleft.all():
        action = 'turnleft'
    if turnright.all():
        action = 'turnright'
    if turnaround.all():
        action = 'turnright'
    print(action)
    new_dir = 0
    if turnaround.all():
        next_dir =np.array([[0, 1],[-1, 0]]) @ cur_dir 
    if next_dir[0] == 1 and next_dir[1] == 0:
        new_dir = 'E'
    if next_dir[0] == -1 and next_dir[1] == 0:
        new_dir = 'W'
    if next_dir[0] == 0 and next_dir[1] == 1:
        new_dir = 'N'
    if next_dir[0] == 0 and next_dir[1] == -1:
        new_dir = 'S'
    return (action, new_dir)

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
        self.path, self.actions = self.find_path()

    def __call__(self, t):

        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE 

        # ------------------

        return self.actions[t]

    def find_path(self):
        path = []
        actions = []
        # find path from sel.loc to self.goal
        # TODO PUT YOUR CODE HERE
        # s - wierzchołek startowy
        # g - wierzchołek docelowy
        # nodes - lista wierzchołków
        # najpierw jest numer wierzchołka, a potem jest koszt
        nodes =  {}
        for place in self.locations:
            nodes[place] = []
            if (place[0]+1, place[1]) in self.locations:
                nodes[place].append((place[0]+1, place[1]))
            if (place[0]-1, place[1]) in self.locations:
                nodes[place].append((place[0]-1, place[1]))
            if (place[0], place[1]+1) in self.locations:
                nodes[place].append((place[0], place[1]+1))
            if (place[0], place[1]-1) in self.locations:
                nodes[place].append((place[0], place[1]-1))
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
        q.put((0,s))
        cost[s] = 0
        # dopóki kolejka nie jest pusta, czyli są jeszcze jakieś wierzchołki do odwiedzenia
        while not q.empty():
            # pobierz wierzchołek o najmniejszym priotytecie i usuń go z kolejki
            cur_n = q.get()
            # przerwij jeśli odwiedzony
            if cur_n[1] in visited:
              continue
            # dodaj wierzchołek do listy odwiedonych
            visited.add(cur_n[1])
            # przerwij jeśli dotarliśmy do celu
            if cur_n[1] == g:
                break
            # dla wszystkich krawędzi z aktualnego wierzchołka    
            for nh in nodes[cur_n[1]]:
                # przerwij jeśli sąsiad był już odwiedzony
                if nh in visited: 
                    continue  
                # pobierz koszt sąsiada lub przypisz mu inf
                old_cost = cost[nh]
                # oblicz koszt dla danego wierzchołka 
                distance = calc_cost(self.dir, cur_n[1][0], cur_n[1][1], nh[0], nh[1])
                new_cost = cost[cur_n[1]] + distance
               # rozważ nową ścieżkę tylko wtedy, gdy jest lepsza niż dotychczas najlepsze ścieżka
                if new_cost < old_cost:
                    # zaktualizuj wartość sąsiada w słowniku kosztów
                    cost[nh] = new_cost
                    # ustaw poprzednika
                    parent[nh] = cur_n[1]
                    # dodaj sąsiada do kolejki
                    q.put((cost[nh], nh))
        # odtwórz ścieżkę
        cur_n = g
        while cur_n is not None:
            path.append(cur_n)
            cur_n = parent[cur_n]
        path.reverse()


        cur_dir = self.dir
        for i in range(len(path)-1):
            while True:
                action,cur_dir = calc_movement(cur_dir, path[i][0], path[i][1], path[i+1][0], path[i+1][1])
                #print(cur_dir, path[i], path[i+1], action)
                print( path[i], path[i+1])
                if action != 'forward':
                    actions.append(action)
                else:
                    actions.append('forward')
                    break
        # ------------------
        print(actions)
        return path, actions

    def get_path(self):
        return self.path

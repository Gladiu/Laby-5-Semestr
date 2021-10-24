import queue 
from math import inf
# s - wierzchołek startowy
# g - wierzchołek docelowy
# nodes - lista wierzchołków
# najpierw jest numer wierzchołka, a potem jest koszt
nodes = {
        1:[(2, 1), (3, 1)],
        2:[(1, 1), (5, 7)],
        3:[(1, 1), (4, 2)],
        4:[(6, 1), (3, 2)],
        5:[(6, 3), (2, 7), (8, 2)],
        6:[(4, 1), (5, 3), (8, 6), (7, 5)],
        7:[(6, 5)],
        8:[(6, 6), (5, 2)]
        }
s = 1
g = 8
# zbiór wierzchołków odwiedzonych
visited = set()
# słownik kosztów
cost = {n: inf for n in nodes}
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
    _, cur_n = q.get()
    # przerwij jeśli odwiedzony
    if cur_n in visited:
      continue
    # dodaj wierzchołek do listy odwiedonych
    visited.add(cur_n)
    # przerwij jeśli dotarliśmy do celu
    if cur_n == g:
        break
    # dla wszystkich krawędzi z aktualnego wierzchołka    
    for nh, distance in nodes[cur_n]:
        # przerwij jeśli sąsiad był już odwiedzony
        if nh in visited: 
            continue  
        # pobierz koszt sąsiada lub przypisz mu inf
        old_cost = cost[nh]
        # oblicz koszt dla danego wierzchołka 
        new_cost = cost[cur_n] + distance
        # rozważ nową ścieżkę tylko wtedy, gdy jest lepsza niż dotychczas najlepsze ścieżka
        if new_cost < old_cost:
            # zaktualizuj wartość sąsiada w słowniku kosztów
            cost[nh] = new_cost
            # ustaw poprzednika
            parent[nh] = cur_n
            # dodaj sąsiada do kolejki
            q.put((new_cost, nh))
# odtwórz ścieżkę
path = []
cur_n = g
while cur_n is not None:
    path.append(cur_n)
    cur_n = parent[cur_n]
path.reverse()
print(path)




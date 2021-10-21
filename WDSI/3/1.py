import queue
import math
# s - wierzchołek startowy
# g - wierzchołek docelowy
# nodes - lista wierzchołków
s = 1
g = 6
# Wartoscia slownika są listy zawierające wierzhołki i cenę w jednej liście
# pierwszy element listy to droga
# drugi element list to nazwa wierzcholka
nodes = {
        1:[[1, 2],[1, 3]],
        2:[[1, 1],[7, 5]],
        3:[[1, 1],[2, 4]],
        4:[[2, 3],[1, 6]],
        5:[[7, 2],[3, 6],[2, 8]],
        6:[[1, 4],[3, 5],[6, 8],[5, 7]],
        7:[[5, 6]],
        8:[[6, 8], [2, 5]]
        }
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
while not empty(q):
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
    for nh, distance in edges(cur_n):
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
            push(q, (new_cost, nh))
# odtwórz ścieżkę
path = []
cur_n = g
while cur_n is not None:
    path.append(cur_n)
    cur_n = parent[cur_n]
path.reverse()

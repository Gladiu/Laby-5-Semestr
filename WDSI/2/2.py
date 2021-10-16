
# s - wierzchołek startowy
# g - wierzchołek docelowy
# nodes - lista wierzchołków

# zbiór wierzchołków odwiedzonych
visited = set()
# słownik kosztów
cost = {n: inf for n in nodes}
# słownik poprzedników
parent = {s: None}
# utwórz kolejke, w której elementy są ułożone nie w kolejności wprowadzania, lecz w kolejności priorytetu.
q = PriorityQueue()
# dodaj wierzchołek startowy
push(q, (0,s))
cost[s] = 0
# dopóki kolejka nie jest pusta, czyli są jeszcze jakieś wierzchołki do odwiedzenia
while not empty(q):
    # pobierz wierzchołek o najmniejszym priotytecie i usuń go z kolejki
    _, cur_n = top(q)
    pop(q)
    # przerwij jeśli odwiedzony
    if cur_n in visited:
      continue
    # dodaj wierzchołek do listy odwiedonych
    add(visited, cur_n)
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
reverse(path)

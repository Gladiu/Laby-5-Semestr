# 2.1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot

# 2.2
def model(x,t):
    return t ** 2

# 2.3
t = np.linspace(0, 5, 1000)
res = odeint(model, [0],t)

# 2.4
res_nume = res[len(res)-1][0] # pobieranie ostatniej liczby z array'a
res_anal = (1.0/3.0) * (5 ** 3)

print(f"Rozwiązanie numeryczne daje nam {res_nume}, rozwiązanie analityczne zwraca {res_anal}")
print(f"Różnica to {abs(res_nume-res_anal)} i jest bardzo mała, jednak rozwiązania nie pokrywają się całkowicie")
print("W funkcji odeint została użyta metoda lsoda z biblioteki FORTAN odepack")


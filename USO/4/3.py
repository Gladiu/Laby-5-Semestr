from math import inf
import numpy as np 
import scipy
from scipy import optimize
import matplotlib.pyplot as plot

# Zadanie 3.1

x = np.linspace(0, 5, 100)

y = x**4 - 4*(x**3) - 2*(x**2) + 12 * x + 9
plot.plot(x, y)
# Korzystając ze znamycch narzędzi
# x^4 - 4x^3 - 2x^2 + 12x + 9 = 0
# Pochodna z funkcji 
# 4x^3 - 12x^2 - 4x + 12 = 0
# x^3 - 3x^2 - x + 3 = 0
# x^3 - 3x^2 - (x - 3) = 0
# (x-3)x^2 - (x-3) = 0
# (x-3)(x^2 -1) = 0
# (x-3)(x-1)(x+1) = 0
# Ekstrema funkcji wynoszą -1 1 i 3
# Ekstremum jest w 3 i wynosi 0


def fun(arguments):
    x, y = arguments
    return x**4 - 4*(x**3) - 2*(x**2) + 12 * x + 9
# Zadanie optymalizacji

bnds = ((0, None), (None, None))
res = scipy.optimize.minimize(fun, (2, 0), method='SLSQP', bounds=bnds)
# Use actual function
print(res)
def fun(x):
    return x**4 - 4*(x**3) - 2*(x**2) + 12 * x + 9
ret = scipy.optimize.dual_annealing(fun, bounds=list(zip([0], [99])))
print(ret)
# Metoda z funkcją minimize jest ogólną metodą na rozwiązanie zadania optymalizacji, gdzie dual_annealing jest funkcją stworzoną wyłącznie do znajdowania ekstremów funkcji
# Obie metody zwróciły poprawne rozwiązania z tym że funkcja minimize zwróciła wartość x i y, gdzie funkcja dual_annealing zwróciła tylko wartość x i nie podała wartości ekstremum
# W poprzednim zadaniu rozwiązanie go funkcją dual_annealing byłoby niemożliwe, gdyż tam chodziło o najmniejszą wartość y, a nie ekstremum jakiejś funkcji
plot.show()

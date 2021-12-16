import numpy as np
import math
from scipy.integrate import odeint
from matplotlib import pyplot

# Zadanie 2.1
def model(z, t):
    z_next0 = z[0] * math.log(z[1])
    z_next1 = -z[1] * math.log(z[0]) + z[1] * 1
    return [ z_next0, z_next1] 

pyplot.figure()
t = np.linspace(0, 2, 1000)
res = odeint(model, [1, 1], t)
pyplot.plot(t, res[:,0])
pyplot.plot(t, res[:,1])

# Zadanie 2.2
def model0(x, t):
    x0 = x[1]
    x1 = -x[0] + 1
    return [x0, x1]

pyplot.figure()
t = np.linspace(0, 2, 1000)
res = odeint(model0, [1, 1], t)
pyplot.plot(t, res[:,0])
pyplot.plot(t, res[:,1])

# Zadanie 2.3
# Odpowiedź skokowa nie pokrywa się bo zlinearyzowaliśmy układ w innym
# punkcie niż podajemy w warunkach początkowych. Mamy też inny układ

# Zadanie 2.4
pyplot.figure()
t = np.linspace(0, 2, 1000)
res = odeint(model0, [0, 0], t)
pyplot.plot(t, res[:,0])
pyplot.plot(t, res[:,1])

# Zadanie 2.5
pyplot.figure()
t = np.linspace(0, 2, 1000)
res = odeint(model0, [0, 0], t)
pyplot.plot(t, np.exp(res[:,0]))
pyplot.plot(t, np.exp(res[:,1]))

# W tym wypadku zmienne stanu się pokrywają ponieważ wróciliśmy do poprzedniego
# układu.


pyplot.show()



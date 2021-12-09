# 2.1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot

kp = 2
omega = 4
sigma = 0.25
u = 1

def model(x,t):
    y = x[0]
    dydt = x[1]
    dy2dt2 = ((-2.0*sigma)/omega) * x[1] + (-1.0/omega) * np.sqrt(x[0]) + (kp / (omega ** 2)) * u
    return [dydt,dy2dt2]

t = np.linspace(0, 100, 1000)
res = odeint(model, [0, 0], t)
plot.plot(t, res[:,0])
plot.plot(t, res[:,1])
# Odpowiedź ma charakter oscylacyjny który się stabilizuje
plot.show()

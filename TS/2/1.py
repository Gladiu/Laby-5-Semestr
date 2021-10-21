import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math

R1 = .2
L = 0.1
C = 0.05
def force(t):
    A = 2
    return 1 * A 

def obj(t, x):
    # x1 = i1
    # x2 = q2
    dx0 = -(R1/L)*x[0]-(1.0/L*C)*x[1]+(1.0/L)*force(t)
    dx1 = x[0]-(0.25*(1.0/C)*x[1])/(5.0-(1.0/C)*x[1])
    return [dx0, dx1]

res = solve_ivp(obj, [0,2], [0,0], rtol=1e-10)

plt.plot(res.t, res.y[0])
plt.plot(res.t, res.y[1])

plt.show()

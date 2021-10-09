import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math

m = 1.0
l = 0.5
J = 0.05
b = [0, 0.1, 0.5]
g = 9.81

def force(t):
    return 0

def obj(t, x):
    # x1 = fi
    # x2 = fi'
    dx0 = x[1]
    dx1 = (-b[0]*x[1] - m*g*l*np.sin(x[0]) + force(t))/(m*l*l+J)
    return [dx0, dx1]



res = solve_ivp(obj, [0,60], [3.14/2.0,0], rtol=1e-10)

#plt.plot(res.t, res.y[0])
#plt.plot(res.t, res.y[1])
#plt.plot(np.sin(res.y[0]), np.cos(res.y[0]))

# Portret fazowy
plt.figure(0)
plt.plot(res.y[0], res.y[1])
plt.show()

plt.figure(1)
for i in range(0, 2):
    def obj(t, x):
        # x1 = fi
        # x2 = fi'
        dx0 = x[1]
        dx1 = (-b[i]*x[1] - m*g*l*np.sin(x[0]) + force(t))/(m*l*l+J)
        return [dx0, dx1]
    res = solve_ivp(obj, [0,60], [3.14/2.0,0], rtol=1e-10)
    plt.plot(res.t, res.y[0])
plt.show()

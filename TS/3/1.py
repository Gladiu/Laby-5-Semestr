import numpy as np
import matplotlib.pyplot as plot
import scipy.signal as sig
from scipy.integrate import solve_ivp

m = 1.0
k = 1.0
b = 0.5

A = np.array([[0, 1.0], [(-k/m), (-b/m)]])
B = np.array([[0], [1.0/m]])
C = np.array([[1.0, 0]])
#
O = np.vstack((C, C@A))
print(np.linalg.matrix_rank(O))

omega = 5

L = np.array([[-2*omega-0.5],[omega*omega-omega - 0.75]])


def force(t):
    return 1

def obj(t, x):
    
    dx0 = x[1] + 1.0/m
    dx1 = -(k/m)*x[0] + (-b/m)*x[1] + (1.0/m)*force(t)
    dx2 = x[3] + 1.0/m + L[0][0]*(x[0]-x[2])
    dx3 = -(k/m)*x[2] + (-b/m)*x[3] + (1.0/m)*force(t) + (omega*omega-omega-0.75)* (x[0]-x[2])
    return [dx0, dx1, dx2, dx3]

res = solve_ivp(obj, [0,10], [0, 0, 0, 0], rtol=1e-10)


plot.figure()
plot.plot(res.t, res.y[0])
plot.plot(res.t, res.y[2])
plot.show()

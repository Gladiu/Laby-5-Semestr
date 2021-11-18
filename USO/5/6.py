import numpy as np
import scipy.signal as sig
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
from matplotlib import pyplot as plot
import sympy as symbolic


L = 0.2
C = 0.5
R = 10

# Parametry regulatora PID
Tp = 2
Ti = 1
Td = 0.4
A = np.array([[0, 1, 0], [0, 0, 1],[1/C, R, L]])
B = np.array([[0],[0], [1]])
C = np.array([[0, 0, 1]])
D = 0
object = sig.StateSpace(A, B, C, D)

plot.figure()
res = sig.step(object)
plot.plot(res[0], res[1])

plot.show()

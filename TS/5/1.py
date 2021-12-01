import numpy as np
import scipy.signal as sig
from scipy.integrate import odeint
from matplotlib import pyplot
import sympy as sym


# Zadanie 1
L = 0.1
R = 5.0
C = 0.01
Vin = 8.0

A = np.array([[0.0, 1.0], [-1.0/(C*L), -1.0/(C*R)]])
B = np.array([[0],[Vin/C*L]])
C = np.array([[1, 0]])

def force(t):
    return 1

def model(x,t):
    x_next = A @ np.array([[x[0]], [x[1]]]) + B * force(t)
    return [x_next[0][0], x_next[1][0]]

t = np.linspace(0, 0.7, 1000)

res = odeint(model, [0, 0], t)

pyplot.figure()
pyplot.plot( t, res[:, 0])
pyplot.plot( t, res[:, 1])
pyplot.show()

# Zadanie 2

l = sym.Symbol('lambda')
eigen_values = sym.solve(sym.Matrix(A - l*np.eye(2)).det())
print(eigen_values)


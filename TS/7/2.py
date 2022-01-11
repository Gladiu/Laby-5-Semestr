import numpy as np 
import sympy as sym
import scipy.signal as sig
from scipy.linalg import solve_continuous_lyapunov
from mpl_toolkits import mplot3d
from scipy.integrate import odeint
import matplotlib.pyplot as plot
L = 0.1
Vin = 8
R = 5
Capacitor = 0.01

A = np.array([[0, 1],[-1/(L*Capacitor),-1/(L*R)]])
B = np.array([[0],[Vin/(Capacitor*L)]])
C = np.array([1, 0])

l = sym.Symbol('lambda')
k1 = sym.Symbol('k1')
k2 = sym.Symbol('k2')

# 2.1
K = np.array([[k1,k2]])
eigen_values = sym.Matrix(l*np.eye(2) - (A-B@K)).det()
#print(eigen_values)

k1 = (-999/8000)
k2 = 0 

# 2.2

K = np.array([[k1,k2]])
H = A-B@K

Q = np.array([[1, 0],[0,1]])
P = solve_continuous_lyapunov(H,Q)

temp = np.linspace(-10,10,1000)
x = np.vstack((temp,temp))

V = 0.5 * x.T @ P @ x
V_prime = -0.5 * x.T @ Q @ x

plot.figure()

ax = plot.axes(projection='3d')
#ax.plot_surface(x,x,V, cmap='viridis', edgecolor='none')
ax.plot_surface(temp,V_prime,V, cmap='viridis', edgecolor='none')

plot.show()


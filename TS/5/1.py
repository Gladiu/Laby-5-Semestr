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



# Zadanie 2

l = sym.Symbol('lambda')
eigen_values = sym.solve(sym.Matrix(A - l*np.eye(2)).det())
print(eigen_values)

# Zadanie 3

def model(x,t):
    x_next = A @ np.array([[x[0]], [x[1]]]) + B * force(t)
    return [x_next[0][0], x_next[1][0]]

def force(t):
    return 1

t = np.linspace(0, 0.7, 1000)
V0 = [0, 5, 7]

pyplot.figure()
for i in range(len(V0)):

    res = odeint(model, [V0[i], 0], t)

    title = "Odpowiedź skokowa układu dla V0 = " + str(V0[i])
    pyplot.subplot(3, 1, i+1)
    pyplot.title(title)
    pyplot.plot( t, res[:, 0])
    pyplot.plot( t, res[:, 1])

pyplot.show()

# Zadanie 4
# e' = A*e - B*u - A*x_d
# e' = A*e - B*(Vd/Vin+ufb) - A*x_d
# e' = A*e - B*(Vd/Vin) - B*u_fb - A*x_d
# e' = A*e - B*u_fb - A*x_d - B*(Vd/Vin)
# e' = A*e - B*u_fb - [[0], [Vd/-C*L]] - B*(Vd/Vin)
# Podstawiamy B = np.array([[0],[Vin/C*L]])
# e' = A*e - B*u_fb - [[0], [Vd/-C*L]] - [[0],[Vd/C*L]]
# e' = A*e - B*u_fb

# Zadanie 5
# e' = Ae-B*K*e
# e' = (A-B*K)*e
k1 = sym.Symbol('k1')
k2 = sym.Symbol('k2')
K = np.array([[k1, k2]])

eigen_values = sym.Matrix((A-B@K) - l*np.eye(2)).det()
#eigen_values[0].sub(l, -5)
desired_eigen_values = [-5, -1, -10]
#for i in range(len(desired_eigen_values)):
i = 0
#print(sym.solve(sym.Eq(desired_eigen_values[i], eigen_values[0]), [k1, k2]))
print(eigen_values.subs(l, -5))

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
B = np.array([[0],[Vin/(C*L)]])
C = np.array([[1, 0]])

k1 = sym.Symbol('k1')
k2 = sym.Symbol('k2')

K = np.array([[k1, k2]])

xd = np.array([[3], [4]])

t = np.linspace(0, 0.7, 1000)

def model0(x,t):
    x_next = A @ np.array([[x[0]], [x[1]]]) + B * force(t)
    return [x_next[0][0], x_next[1][0]]

def force(t):
    return 1

#pyplot.plot( t, res[:, 0])
#pyplot.plot( t, res[:, 1])

# Zadanie 2

def generator(t):
    #             Vd             Vd'
    return (3 + 2*np.sin(t), 2*np.cos(t))

# Zadanie 3

l = sym.Symbol('lambda')
eigen_values = sym.Matrix((A-B@K) - l*np.eye(2)).det()

print(eigen_values)

# k1 = dowolne
# k2 = (omega_c - 10)/4000

# - Należy dobrać tak wc aby czas narastania był szybki ale żeby przeregulowanie było małe
#   nalepiej żeby to nie były liczby zespolone i żeby wc było możliwie małe
# - Sterownik nie zadziała dla wc w prawej półpłaszyźnie zespolonej

# Zadanie 4
for omega_c in [5, 10, 25]:
    pyplot.figure()
    pyplot.title("omega_c = " + str(omega_c))
    K = np.array([[1, (omega_c - 10)/4000]])
    
    def model1(x, t):
        xd = np.array([[3], [4]])
        x = np.array([[x[0]], [x[1]]]) 
        e = xd - x
        (Vd,Vd_prime) = generator(t)
        x_primeprime = 0
        u = K @ e + Vd/Vin + (L*Vd_prime)/(R*Vin) + (C*L*x_primeprime)/Vin
    pyplot.subplot(1,2,1)

    res = odeint(model1, [0,0], t)
    pyplot.plot( t, res[:, 0])
    pyplot.plot( t, res[:, 1])

    pyplot.subplot(1,2,2)
    res = odeint(model1, [3,4], t)
    pyplot.plot( t, res[:, 0])
    pyplot.plot( t, res[:, 1])

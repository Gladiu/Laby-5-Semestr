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

k1 = sym.Symbol('k1')
k2 = sym.Symbol('k2')

K = np.array([[k1, k2]])

xd = np.array([[3], [4]])

t = np.linspace(0, 15, 1000)

def model0(x,t):
    x_next = A @ np.array([[x[0]], [x[1]]]) + B * force(t)
    return [x_next[0][0], x_next[1][0]]

def force(t):
    return 1
#pyplot.figure()
#res = odeint(model0, [0,0], t)
#pyplot.plot( t, res[:, 0])
#pyplot.plot( t, res[:, 1])

# Zadanie 2

def generator(t):
    #             Vd             Vd'          Vd''
    t = 2*t
    return (3 + 2*np.sin(t), 2*np.cos(t), -2*np.sin(t))

# Zadanie 3

l = sym.Symbol('lambda')
eigen_values = sym.Matrix((A-B@K) - l*np.eye(2)).det()

print(eigen_values)

# k1 = (omega_c ** 2 - 1000)/(8000)
# k2 = (2 * omega_c - 20)/8000

# - Należy dobrać tak wc aby czas narastania był szybki ale żeby przeregulowanie było małe
#   nalepiej żeby to nie były liczby zespolone i żeby wc było możliwie małe
# - Sterownik nie zadziała dla wc w prawej półpłaszyźnie zespolonej

# Zadanie 4
for omega_c in [5.0, 10.0, 25.0]:
    pyplot.figure()
    title = "omega_c = " + str(omega_c)
    print(title)
    K = np.array([[(omega_c ** 2 - 1000)/(8000.0) , (omega_c - 10)/4000.0]])
    
    def model1(x, t):
        (Vd,Vd_prime, Vd_prime_prime) = generator(t)
        xd = np.array([[Vd], [Vd_prime]])
        x = np.array([[x[0]], [x[1]]]) 
        e = xd - x
        u = (K @ e)[0][0] + Vd/Vin + (L*Vd_prime)/(R*Vin) #+ (C*L*Vd_prime_prime)/Vin
        x_next = A @ x + B * u
        return [x_next[0][0], x_next[1][0]]

    pyplot.subplot(1,2,1)
    (ref_traj, ref_traj_prime, ref_traj_prime_prime) = generator(t)
    
    res1 = odeint(model1, [0,0], t)
    res2 = odeint(model1, [3,4], t)


    pyplot.title(title)
    pyplot.plot( t, res1[:, 0])
    pyplot.plot( t, res2[:, 0])
    pyplot.plot( t, ref_traj)

    pyplot.title(title)
    pyplot.subplot(1,2,2)
    pyplot.plot( t, res1[:, 1])
    pyplot.plot( t, res2[:, 1])
    pyplot.plot( t, ref_traj_prime)
pyplot.show()

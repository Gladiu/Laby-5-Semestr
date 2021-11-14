import numpy as np
import matplotlib.pyplot as plot
import scipy.signal as sig
from scipy.integrate import solve_ivp

# Object parameters
m = 1.0
k = 1.0
b = 0.5

A = np.array([[0, 1.0], [(-k/m), (-b/m)]])
B = np.array([[0], [1.0/m]])
C = np.array([[1.0, 0]])

# Observer Parameters
O = np.vstack((C, C@A))
omega = 50
L = np.array([[2*omega-0.5],[omega*omega-omega - 0.75]])

# Simulation parameters
mu, sigma = 0, 0.10 # mean and standard deviation
t_max = 10.0

def force(t):
    return 1

def obj(t, x):
    noise  = np.random.normal(mu, sigma)
    x_normal = A @ np.array([[x[0]],[x[1]]]) + B * force(t)
    x_est = A @ np.array([[x[0]],[x[1]]]) + B * force(t) + L@(x[0]+noise - C @ np.array([[x[2]],[x[3]]]))
    return [x_normal[0][0], x_normal[1][0], x_est[0][0], x_est[1][0]]

res = solve_ivp(obj, [0, t_max], [0, 0, 1, 0], rtol=1e-2)

plot.figure()
plot.plot(res.t, res.y[0])
plot.plot(res.t, res.y[2])
plot.show()

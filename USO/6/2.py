import numpy as np
import scipy.signal as sig
import scipy.linalg as linalg
import scipy.integrate as integ
import matplotlib.pyplot as plot

R = 0.5
C = 0.5
L = 0.2
A = np.array([[0, 1], [-1/(L*C), -R/L]])
B = np.array([[0],[1/L]])
# 2.5
# Nie ma zależności pomiędzy dobranymi wartościami do Q oraz R
# Q i R natomiast wpłwają na wskaźnik jakości j
Q = np.eye(2)
R = np.eye(1)

# 2.1
P = linalg.solve_continuous_are(A, B, Q, R)

# 2.4
K = R @ B.T @ P

# 2.2
j = []
def model(x,t):
    x = np.array(x)
    u = -K @ x
    x_next = A@np.array([[x[0]],[x[1]]]) + B @ u
    j.append(x.T @ Q @ x + u.T @ R @ u)
    return [x_next[0][0],x_next[1][0]]

t = np.linspace(0, 5, 100)
res = integ.odeint(model, [1, 0], t)
plot.plot(t, res[:, 0])
plot.plot(np.linspace(0, 5, len(j)), j)




plot.show()

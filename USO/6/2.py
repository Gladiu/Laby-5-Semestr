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
#K = np.linalg.inv(R) @ B.T @ P
K = R @ B.T @ P
# 2.2
j = []
def model(x,t):
    x = np.array(x)
    u = -K @ x
    x_next = A@np.array([[x[0]],[x[1]]]) + B @ u
    j.append(x.T @ Q @ x+ u.T @ R @ u)
    return [x_next[0][0],x_next[1][0]]

t = np.linspace(0, 5, 100)
res = integ.odeint(model, [1, 0], t)
plot.plot(t, res[:, 0])
plot.plot(t, res[:, 1])
for i in range(len(j)):
    if i >0:
        j[i] = j[i-1] + j[i]
plot.plot(np.linspace(0, 5, len(j)), j)

# 2.7
plot.figure()

j = []
qd = 5.0
xd = np.array([[qd], [0]])
uarray = []
def model_modded(x,t):
    x = np.array(x)
    e = xd - np.array([[x[0]],[x[1]]])
    ue = -K @ e
    u = -ue + (qd/(C)) # W instrukcji we wzorze numer 10 jest nieścisłość jest napisane 1/C
    x_next = A@np.array([[x[0]],[x[1]]]) + B @ u
    j.append(e.T @ Q @ e + ue.T @ R @ ue)
    return [x_next[0][0],x_next[1][0]]

t = np.linspace(0, 5, 100)
res = integ.odeint(model_modded, [0, 0], t)
plot.plot(t, res[:, 0])
plot.plot(t, res[:, 1])
#plot.plot(np.linspace(0, 5, len(j)), j)
for i in range(len(j)):
    if i >0:
        j[i] = j[i-1] + j[i]
print(j)
plot.show()

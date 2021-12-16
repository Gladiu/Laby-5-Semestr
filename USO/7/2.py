import numpy as np
import scipy.interpolate as interp
import scipy.integrate as integ
import matplotlib.pyplot as plot 

R = 0.5
C = 0.5
L = 0.2

A = np.array([[0, 1],[-1/(L*C), -R/L]])
B = np.array([[0], [1/L]])
R = np.eye(1)
Q = np.eye(2)
S = np.eye(2)

# 2.1
def riccati(p,t):
    p = np.array([[p[0], p[1]],[p[2], p[3]]])
    next_p = p @ A - p @ B @ np.linalg.inv(R) + A.T @ p + Q
    return [next_p[0][0], next_p[0][1], next_p[1][0], next_p[1][0]]


# 2.2
t = np.linspace(0, 5, 100)
P = integ.odeint(riccati, [0,0,0,0], t)
plot.figure()
plot.title("Wartości macierzy P w czasie")
plot.subplot(2,2,1)
plot.plot(t, P[:, 0])
plot.subplot(2,2,2)
plot.plot(t, P[:, 1])
plot.subplot(2,2,3)
plot.plot(t, P[:, 2])
plot.subplot(2,2,4)
plot.plot(t, P[:, 3])

# 2.3
# W instrukcji nie ma napisane że trzeba dać fill_value, bez tego kod nie dziala
P_0 = interp.interp1d(t, P[:,0], fill_value='extrapolate')
P_1 = interp.interp1d(t, P[:,1], fill_value='extrapolate')
P_2 = interp.interp1d(t, P[:,2], fill_value='extrapolate')
P_3 = interp.interp1d(t, P[:,3], fill_value='extrapolate')

J1 = []
J2 = []
J = []
t = np.linspace(0, 5, 100)
def model(x,t):
    x = np.array([[x[0]], [x[1]]])
    current_p = np.array([[P_0(t), P_1(t)],[P_2(t), P_3(t)]])
    K = np.linalg.inv(R) @ B.T @ current_p
    u =  np.array(-K @ x)
    x_next = A @ x + B @ u
    x_next = np.array([x_next[0][0], x_next[1][0]])
    x_dla_J = np.array([[x_next[0]],[x_next[1]]])
    J1.append((x_dla_J.T @ current_p @ x_dla_J)[0][0])
    J2.append((sum(J2) + x_dla_J.T @ Q @ x_dla_J + u.T @ R @ u)[0][0])
    return x_next

for i in range(len(J1)):
    J.append(J1[i]+J2[i])

plot.figure()
res = integ.odeint(model, [1, 1], t) # w instrukcji nie ma wartości początkowych bez których kod nie działa
plot.plot(t, res[:,0])
plot.plot(t, res[:,1])
print(J)
#plot.plot(t, J)

plot.show()

import numpy as np 
import matplotlib.pyplot as plot
import scipy.signal as sig

tf1 =  sig.TransferFunction([1.0], [1.0, 1.0, 2.0])
tf2 =  sig.TransferFunction([1.0], [1.0, -4.0, 2.0, 5.0])
tf3 =  sig.TransferFunction([1.0], [1.0, 6.0, 4.5, -5.0, -6.0])

ss1 = sig.StateSpace(np.array([[-4.0, -1.0], [-2.0, -1.0]]), np.array([[2.0],[1.0]]), np.array([3.0, -4.0]), 0)
ss2 = sig.StateSpace(np.array([[-1.0, 0.0, 1.0], [-6, 3, 5.0], [-5.0, -2.0, 4.0]]), np.array([[0], [1.0], [10.0]]), np.array([1.0, 1.0, 1.0]), 0)
ss3 = sig.StateSpace(np.array([[-3.0,1.25, -0.75, -2.75], [-6.0, 3.0, -3.5, -6.0], [0.0, -1.0, 0.0, 1.0], [-6.0, 5.0, -4.5, -6.0]]), np.array([[0.5], [1.0], [0.0], [1.0]]), np.array([2.0, 0, 0, 0]), 0)

ss11 = sig.ss2tf(ss1.A, ss1.B, ss1.C, ss1.D)
ss21 = sig.ss2tf(ss2.A, ss2.B, ss2.C, ss2.D)
ss31 = sig.ss2tf(ss3.A, ss3.B, ss3.C, ss3.D)

t = np.linspace(0, 20, 100)
u = np.sin(t)

plot.figure()
plot.title("System pierwszy")
res = sig.step(tf1)
res = sig.lsim(tf1, u, t)
plot.plot(res[0], res[1])
res = sig.step(ss1)
res = sig.lsim(ss1, u, t)
plot.plot(res[0], res[1])
res = sig.step(ss11)
res = sig.lsim(ss11, u, t)
plot.plot(res[0], res[1])

plot.figure()
plot.title("System drugi")
res = sig.step(tf2)
plot.plot(res[0], res[1])
res = sig.step(ss2)
plot.plot(res[0], res[1])
res = sig.step(ss21)
plot.plot(res[0], res[1])

plot.figure()
plot.title("System trzeci")
res = sig.step(tf3)
plot.plot(res[0], res[1])
res = sig.step(ss3)
plot.plot(res[0], res[1])
res = sig.step(ss31)
plot.plot(res[0], res[1])

plot.show()


# Wyniki są drastycznie różne, możliwe jest otrzymanie różnychh wyników, transmitancja jest stosunkiem wejścia do wyjścia, zachhowując ten stosunek możemy otrzymać różne odpowiedzi

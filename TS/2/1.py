import numpy as np 
import matplotlib.pyplot as plot
import scipy.signal as sig

tf1 =  sig.TransferFunction([10.0], [1.0, 2.0])
tf2 =  sig.TransferFunction([4.0], [2.0, 0, 1.0])
tf3 =  sig.TransferFunction([-2.0, 6.0], [1.0, 7.0, 16.0, 12.0])

ss1 = sig.StateSpace(np.array([-2.0]), np.array([10.0]), 1, 0)
ss2 = sig.StateSpace(np.array([[0.0, 1.0], [-0.5, 0.0]]), np.array([[0],[2.0]]), np.array([0.0, 1.0]), 0)
ss3 = sig.StateSpace(np.array([[0, 1.0, 0], [0, 0, 1.0], [-12.0, -16.0, 7.0]]), np.array([[0], [-2.0], [20.0]]), np.array([1.0, 0, 0]), 0)

ss11 = sig.tf2ss(tf1.num, tf1.den)
ss21 = sig.tf2ss(tf2.num, tf2.den)
ss31 = sig.tf2ss(tf3.num, tf3.den)

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
res = sig.lsim(tf2, u, t, np.array([[0,10]]))
plot.plot(res[0], res[1])
res = sig.step(ss2)
res = sig.lsim(ss2, u, t, np.array([[0,10]]))
plot.plot(res[0], res[1])
res = sig.step(ss21)
res = sig.lsim(ss21, u, t, np.array([[0.0, 10.0]]))
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

# Z jednej transmitancji możemy otrzymać różne równania stanu, jak w przypadku przykładu trzeciego gdzie widzimy gwałtowne wzrosty przy odpowiedzi skokowej
# Natomiast konwersja z równań stanu do transmitancji jest zawsze tka sama
# Trajektorie zmiennych stanu są różne w transmitancji, ponieważ przy konwersji na równania stanu możemy sobie dowolnie obrać co jest zmienną stanu
# Warunki początkowe różnią się w obu reprezentacjach, przy transmitancji możemy jedynie zmieniać wielkość wymuszenia, ponieważ nie możemy "ustawić" stanu układu jak ma to miejsce w równaniach stanu

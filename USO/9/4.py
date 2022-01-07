import numpy as np
import scipy.signal as sig
from scipy.integrate import odeint
from matplotlib.pyplot import plot,show,title,figure,legend

# 4.1
R = 1.0
m = 9.0
J = 1.0
g = 10.0
d = 0.5
def nonlinear_pendulum(x,t):
    u = 1.0
    x0 = x[1]
    x1 = u/J - (d*x[1])/J - (m*g*R*np.sin(np.deg2rad(x[0])))/J
    return [x0, x1]

t = np.linspace(0, 20, 10000)
res = odeint(nonlinear_pendulum, [0, 0], t)
#title("Model niezlinearyzowany")
#plot(t,res[:,0])
#plot(t,res[:,1])

# 4.2
A = np.array([[0 ,1], [-(m*g*R)/J, -(d/J)]])
B = np.array([[0],[1/J]])
C = np.array([[1, 0]])
D = 0
linearised_model = sig.StateSpace(A,B,C,D)

for u in [0, 5, 20, 45*np.sqrt(2), 70]:
    figure()

    # Symulacja modelu niezlinearyzowanego
    def nonlinear_pendulum_loop(x,t):
        x0 = x[1]
        x1 = u/J - (d*x[1])/J - (m*g*R*np.sin(np.deg2rad(x[0])))/J
        return [x0, x1]
    
    res = odeint(nonlinear_pendulum_loop, [0, 0], t)
    plot(t, res[:,0], label="Niezlinearyzowany x")


    # Symulacja modelu zlinearyzowanego
    u_array = np.ones(len(t))*u
    tout ,yout, xout = sig.lsim(linearised_model, u_array, t)
    plot(tout, yout, label="Zlinearyzowany x")

    legend(loc='best')
    title("Wymuszenie u = "+str(u))

# Model zlinearyzowany odzwierciedla model niezlinearyzowany dla każdego wymuszenia
# tylko to odzwierciedlenie ma miejsce dla niewielkiego otoczenia obranego punktu pracy.
# Dla mniejszych wymuszeń dłużej jesteśmy w otoczeniu tego punktu

# 4.4

S = np.hstack((B, A@B))
if len(A[0]) == np.linalg.matrix_rank(S):
    print("Układ jest sterowalny")
else:
    print("Układ jest nie sterowalny")

# 4.5

A = np.array([[0 ,1], [-(m*g*R)/(J * np.sqrt(2)), -(d/J)]])
B = np.array([[0],[1/J]])
C = np.array([[1, 0]])
D = 0
linearised_model = sig.StateSpace(A,B,C,D)

# 4.6
# Odpowiedzi układów nie pokrywają się, ponieważ linearyzacja nastąpiła w innym punkcie niż (0,0)
# aby odpowiedź się pokrywała powinniśmy przenieść początek układu zlinearyzowanego w punkt w którym
# nastąpiła linearyzacja.
for u in [45 * np.sqrt(2),45 * np.sqrt(2) + 2, 45 * np.sqrt(2) + 10, 45 * np.sqrt(2) + 30 ]:
    figure()

    # Symulacja modelu niezlinearyzowanego
    def nonlinear_pendulum_loop(x,t):
        x0 = x[1]
        x1 = u/J - (d*x[1])/J - (m*g*R*np.sin(np.deg2rad(x[0])))/J
        return [x0, x1]
    
    res = odeint(nonlinear_pendulum_loop, [0, 0], t)
    plot(t, res[:,0], label="Niezlinearyzowany x")


    # Symulacja modelu zlinearyzowanego
    u_array = np.ones(len(t))*u
    tout ,yout, xout = sig.lsim(linearised_model, u_array, t)
    plot(tout, yout, label="Zlinearyzowany x w punkcie (Pi/4, 0)")

    legend(loc='best')
    title("Wymuszenie u = "+str(u))
show()

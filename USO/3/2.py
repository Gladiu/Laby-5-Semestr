import numpy as np
import scipy.signal as sig 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plot 
A = []
B = []
# Rysunek 1 niesterowalny
A.append(np.array([[.5, 0], [0, .5]]))
B.append(np.array([[0.5], [0.25]]))

# Rysunek 2 sterowalny
A.append(np.array([[-1, 0, 0], [0, -0.5, 0], [0, 0, -1/3]]))
B.append(np.array([[1], [1], [1]]))


As = []
As.append(np.array([[0 , 1], [-0.25, 1]]))
As.append(np.array([[0 , 1, 0], [0, 0, 1], [-1/6, -1, -11.0/6.0]]))

Bs = []
Bs.append(np.array([[0],[1]]))
Bs.append(np.array([[0],[0],[1]]))

P = []
#P.append(np.linalg.inv (np.hstack((B[0], A[0] @ B[0])) @ np.linalg.inv(np.hstack((Bs[0], As[0] @ Bs[0])))))
# Wyznaczenie postaci normalnej regulatorowej jest niemożliwe dkla ukłładów niesterowalnych. Niemożliwym jest odwrócenie jednej macierzy przy wyznaczaniu macierzy P

left_side = np.hstack((np.hstack((B[1], A[1] @ B[1])),  A[1]@A[1]@B[1]))
right_side = np.hstack((np.hstack((Bs[1], As[1] @ Bs[1])), As[1]@As[1]@Bs[1]))
P = left_side @ np.linalg.inv(right_side)


for i in range(2):
    title = "Układ z rysunku "
    title = title + str(i+1)
    plot.figure(title)
    plot.title(title)
    response = []
    if i == 1:
        sys = sig.StateSpace(A[i], B[i], np.array([[0, 0, 1]]), 0) 
        response = sig.step(sys)
        plot.plot(response[0], response[1])
        sys = sig.StateSpace(P@As[i]@np.linalg.inv(P), P@B[i], np.array([[0, 0, 1]])@np.linalg.inv(P), 0)
        response = sig.step(sys)
        plot.plot(response[0], response[1])
    if i == 0:
        sys = sig.StateSpace(A[i], B[i], np.array([[1, 0]]), 0) 
        response = sig.step(sys)
        plot.plot(response[0], response[1])
    plot.show()

# Obie reprezentacje nie są równowazne
# Odpowiedź układu w postaci normalnej regulatorowej ustala się na -1 co trzeba wziąć pod uwagę przy projektowaniu układu regulacji

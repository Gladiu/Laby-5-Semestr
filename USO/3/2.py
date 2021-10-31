import numpy as np
import scipy.signal as sig 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plot 
A = []
B = []
# Rysunek 1 niesterowalny
# u = 1 \integral(i_1) + i_1*2 
# 1 \integral(i_1) + i_1*2 = 2 \integral(i_2) + i_2*4
#
# u = q_1+ 2*q_1'
# q_1+ 2*q_1' = 2 * q_2 + 4*q_2'
# 
# Po podstawieniu
# q_1' = -0.5*q_1 + 0.5 * u
# q_2' = 0.5 *q_2 + 0.25*u 
A.append(np.array([[.5, 0], [0, .5]]))
B.append(np.array([[0.5], [0.25]]))

# Rysunek 2 sterowalny
# u = q_1 + q_1'
# q_1 + q_1' = 0.5*q_2 + q_2'
# 0.5*q_2 + q_2' = q_3/3 + q_3'
#
# Po podstawieniu
# q_1' = -q_1 + u
# q_2' = -0.5*q_2 + u
# q_3' = -q_3/3 + u 
A.append(np.array([[-1, 0, 0], [0, -0.5, 0], [0, 0, -1/3]]))
B.append(np.array([[1], [1], [1]]))

# Rysunek 3 nie sterowalny

A.append(np.array([[0, 0, 0],[0, -0.5, 0.5], [0, 0.5, -0.5]]))
B.append(np.array([[1.0], [0.5], [0.5]]))

# Rysunek 4 sterowalny

A.append(np.array([[-6, 0], [1, 0]]))
B.append(np.array([[1], [0]]))

As = []
As.append(np.array([[0 , 1], [-0.25, 1]]))
As.append(np.array([[0 , 1, 0], [0, 0, 1], [1/6, 1]))



for i in range(4):
    title = "Układ z rysunku "
    title = title + str(i+1)
    plot.figure(title)
    plot.title(title)
    response = []
    if i == 1 or i == 2:
        sys = sig.StateSpace(A[i], B[i], np.array([[0, 0, 1]]), 0) 
        response = sig.step(sys)
    if i == 0 or i == 3:
        sys = sig.StateSpace(A[i], B[i], np.array([[1, 0]]), 0) 
        response = sig.step(sys)
    plot.plot(response[0], response[1])
    plot.show()

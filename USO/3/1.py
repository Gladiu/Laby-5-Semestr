import numpy as np
import scipy.signal as sig 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plot 
A = []
B = []
# 1.1 Cechą układu pozwalają decydować o jego sterowalności jest warunek mówiący o tym, że macierz Kalmana układu musi mieć pełen rząd
# 1.1 Charakter odpowiedzi układów sterowalnych jest przewidywalny i może osiągnąć każdą wartość

# 1.2 Tak, możliwe jest otrzymanie innych równoważnyh modeli w przestrzeni zmiennych stanów
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
# u = q_1' + q_1'
# q_1' = q_2' + q_2
# q_1' + q_2 = q_3'
#
# q_1' = 0.5 * u
# q_2' = q_1' - q_2
# q_3' = q_2 + q_1'
#
# q_1' = 0.5 * u
# q_2' = 0.5 * u + q_2
# q_3' = 0.5 * u - q_2

A.append(np.array([[0, 0, 0],[0, 1, 0], [0, -1, 0]]))
B.append(np.array([[0.5], [0.5], [0.5]]))

# Rysunek 4 sterowalny
# u = 3*q_1' + 0.5*q_1'' 
# q_2'' = q_1'
# q_2'' = 2*q_3
#
# q_1'' = -6q_1' + u
# q_3 = 0.5 * q_1'
# Przyjmujemy że q_2 i q_3 byłyby obecne w maciezy A tylko wtedy jeśli chcielibyśmy je obserwować
# Więc równania będą pierwszego rzędu gdyż nie mamy powiedzine którą zmienną będziemy obserwować
A.append(np.array([[-6, 0], [1, 0]]))
B.append(np.array([[1], [0]]))

K = [[],[],[],[]]

K[0] = np.hstack((B[0], A[0]@B[0]))
print(np.linalg.matrix_rank(K[0]))

K[1] = np.hstack((B[1], A[1]@B[1]))
K[1] = np.hstack((K[1], A[1]@A[1]@B[1]))
print(np.linalg.matrix_rank(K[1]))

K[2] = np.hstack((B[2], A[2]@B[2]))
K[2] = np.hstack((K[2], A[2]@A[2]@B[2]))
print(np.linalg.matrix_rank(K[2]))

K[3] = np.hstack((B[3], A[3]@B[3]))
print(np.linalg.matrix_rank(K[3]))

# 1.4
for i in range(4):
    title = "Układ z rysunku "
    title = title + str(i+1)
    plot.figure(title)
    plot.title(title)
    if i == 1 or i == 2:
        sys = sig.StateSpace(A[i], B[i], np.array([[1, 0, 0]]), 0) 
        response = sig.step(sys)
    if i == 0 or i == 3:
        sys = sig.StateSpace(A[i], B[i], np.array([[1, 0]]), 0) 
        response = sig.step(sys)
    plot.plot(response[0], response[1])
    plot.show()

import numpy as np
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
A1 =  np.array([[.5, 0], [0, .5]])
B1 = np.array([[0.5], [0.25]])

# Rysunek 2 sterowalny
# u = q_1 + q_1'
# q_1 + q_1' = 0.5*q_2 + q_2'
# 0.5*q_2 + q_2' = q_3/3 + q_3'
#
# Po podstawieniu
# q_1' = -q_1 + u
# q_2' = -0.5*q_2 + u
# q_3' = -q_3/3 + u 
A2 = np.array([[-1, 0, 0], [0, -0.5, 0], [0, 0, -1/3]])
B2 = np.array([[1], [1], [1]])

# Rysunek 3 nie sterowalny
# u = q_1'-q_1'
# q_1' = q_2' - q_2
# q_2 = q_3' - q_1'

# Rysunek 4 sterowalny
# TODO dokończyć wyznaczanie macierzy 

K1 = np.hstack((B1, A1@B1))
print(np.linalg.matrix_rank(K1))

K2 = np.hstack((B2, A2@B2))
K2 = np.hstack((K2, A2@A2@B2))
print(np.linalg.matrix_rank(K2))

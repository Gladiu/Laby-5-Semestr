from re import L
import numpy as np 
import scipy.signal as sig 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plot 

if __name__ == "__main__":
    m = 1
    L = 0.5
    d = 0.1
    J = 1.0/3.0
    A = np.array([[-d/J, 0], [0, 1]])
    B = np.array([[1.0/J],[0]])
    C = np.array([[1, 0]])
    D = 0
    sys = sig.StateSpace(A, B, C, D)
    step_response = sig.step(sys)
    plot.plot(step_response[0], step_response[1])
    # Charakter odpowiedzi skokowej jest stabilny, narasta do pewnego momentu i sie stabilizuje
    U = []
    for i in range(11):
        U.append(0.1*i)

    response = sig.lsim2((A,B,C,D), U, range(0, 11))
    plot.plot(response[0], response[1])
    # Charakter odpowiedzi narasta wykladniczo i podaza za liniowym charakterem wymuszenia

    plot.title("Odpowiedzi skokowe")
    w,mag,phase = sig.bode((A, B, C, D))
    plot.figure()
    plot.title("Wykres Wzmocnienia")
    plot.semilogx(w, mag)
    plot.figure()
    plot.title("Wykres Fazowy")
    plot.semilogx(w, phase)
    plot.show()
    # Odpowiedzi odpowiadaja typowi obiektu


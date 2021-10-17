import numpy as np 
import scipy.signal as sig 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plot 



if __name__=="__main__":
    R = 12.0
    L = 0.15
    C = 0.0001
    # 3.1
    num = [1, 0]
    dem = [L, R, (1.0/C)]
    sysTF = sig.TransferFunction(num, dem)

    responseStep = sig.step(sysTF)
    plot.plot(responseStep[0], responseStep[1])
    
    responsePulse = sig.impulse(sysTF)
    plot.plot(responsePulse[0], responsePulse[1])
    
    # 3.2 Wykresy sie pokrywaja
    A = np.array([[0, 1],[(-1.0/(L*C)), -R/L]])
    B = np.array([[0], [1.0/L]])
    C = np.array([0, 1])
    D = 0
    
    sysSS = sig.StateSpace(A, B, C, D)

    responseStep = sig.step(sysSS)
    plot.plot(responseStep[0], responseStep[1])

    responsePulse = sig.impulse(sysSS)
    plot.plot(responsePulse[0], responsePulse[1])

    # 3.3 
    sysSS2 = sig.tf2ss(num, dem)
    sysTF2 = sig.ss2tf(A, B, C, D)
    
    responseStep = sig.step(sysTF2)
    plot.plot(responseStep[0], responseStep[1])
    
    responsePulse = sig.impulse(sysTF2)
    plot.plot(responsePulse[0], responsePulse[1])

    responseStep = sig.step(sysSS2)
    plot.plot(responseStep[0], responseStep[1])

    responsePulse = sig.impulse(sysSS2)
    plot.plot(responsePulse[0], responsePulse[1])
    # Odpowiedzi sie pokrywaja w wiekszosci.
    # Gdyby odpowiedzi sie nie pokrywaly te przeksztalcenia nie mialby sensu
    # Przeksztalcenia sa jednoznaczne
    plot.show()

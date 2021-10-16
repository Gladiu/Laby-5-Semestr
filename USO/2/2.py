import numpy as np 
import scipy.signal as sig 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plot 




def model(t, y):
    T = 2.0
    kp = 3.0
    u = 1.0
    return ((-1/T)*y+(kp/T)*u) 


if __name__=="__main__":
    kp = 3
    T = 2
    A = -1/T
    B = kp/T
    C = 1
    D = 0

    #plot.figure()
    sys = sig.TransferFunction(np.array([kp]), np.array([T, 1]))
    responseTF = sig.step(sys)
    plot.plot(responseTF[0], responseTF[1])
    # Odpowiedx skokowa odpowiada teoretycznym zalozeniom

    sys = sig.StateSpace(A, B, C, D)
    responseSS = sig.step(sys)
    plot.plot(responseSS[0], responseSS[1])
    
    t = range(0, 15)

    #plot.show()
    sys = solve_ivp(model, [0, 15], [0])
    plot.plot(sys.t, sys.y[0])
    plot.show()

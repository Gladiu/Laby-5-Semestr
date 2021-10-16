import numpy as np 
import scipy.signal as sig 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plot 



if __name__=="__main__":
    R = 12
    L = 1
    C = 0.0001

    sys = sig.TransferFunction(np.array([1, 0]), np.array([L, R, 1.0/C]))
    
    responseStep = sig.step(sys)
    plot.plot(responseStep[0], responseStep[1])
    plot.show()
    
    responsePulse = sig.impulse(sys)
    plot.plot(responsePulse[0], responsePulse[1])
    


    plot.show()

import numpy as np
import scipy.signal as sig
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
from matplotlib import pyplot as plot

def main():
    # Parametry układu
    L = 0.2
    C = 0.5
    R = 10

    # Parametry regulatora PID
    Kp = 2
    Ti = 1
    Td = 0.4

    simulated_object = sig.TransferFunction([1],[L, R, 1/C])

    # Parameters of regulator
    regulator = sig.TransferFunction([Td*Ti*Kp, Ti*Kp, Kp], [Ti, 0])

    open_loop = sig.TransferFunction(np.polymul(regulator.num, simulated_object.num),  np.polymul(regulator.den, simulated_object.den))
    closed_loop = sig.TransferFunction([open_loop.num], np.polyadd(open_loop.den, open_loop.num))
    t = np.linspace(0, 15, 1000)
    u = np.ones(len(t))
    #plot.figure()
    #res = sig.lsim(closed_loop, u, t)
    #plot.plot(res[0], res[1])
    plot.figure()
    res = sig.step(closed_loop)
    plot.plot(res[0], res[1])
    plot.show()
    # Uklad z losowo dobranymi parametrami jest stabilny
if __name__=='__main__':
    main()

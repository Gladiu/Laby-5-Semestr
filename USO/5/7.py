import numpy as np
import scipy.signal as sig
from matplotlib import pyplot as plot

def find_nearest_index(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx

def main():
    
    # G(S) = 5/(S^3 + 3S^2 + 3S + 1)
    simulated_object = sig.TransferFunction([5],[1, 3, 3, 1])

    Kg = 1.6# Wzmocnienie graniczne
    Ti = 1000
    Td = 0.001
    # Parameters of regulator
    regulator = sig.TransferFunction([Td*Ti*Kg, Ti*Kg, Kg], [Ti, 0])

    open_loop = sig.TransferFunction(np.polymul(regulator.num, simulated_object.num),  np.polymul(regulator.den, simulated_object.den))
    closed_loop = sig.TransferFunction([open_loop.num], np.polyadd(open_loop.den, open_loop.num))

    plot.figure()
    plot.title("Step response of an object")
    t = np.linspace(0, 50, 1000)
    u = np.ones(len(t))
    res = sig.lsim(closed_loop, u, t)
    plot.plot(res[0], res[1])
    # Zieger nichols 2
    Tosc = 5.6
    Kp = 1.6*Kg
    Ti = Tosc * 0.5
    Td = Tosc * 0.125
    # Parameters of regulator
    regulator = sig.TransferFunction([Td*Ti*Kp, Ti*Kp, Kp], [Ti, 0])

    open_loop = sig.TransferFunction(np.polymul(regulator.num, simulated_object.num),  np.polymul(regulator.den, simulated_object.den))
    closed_loop = sig.TransferFunction([open_loop.num], np.polyadd(open_loop.den, open_loop.num))

    plot.figure()
    plot.title("Zieger Nichols 2")
    res = sig.step(closed_loop)
    ITSE = []
    for i in range(len(res[1])):
        e = 1 -  res[1][i]
        if i > 0:
            ITSE.append(res[0][i] *e*e + ITSE[i-1])
        else:
            ITSE.append(res[0][i] * e * e )
    plot.plot(res[0], res[1])
    plot.figure()
    plot.title("ITSE of Zieger Nichols 2")
    plot.plot(res[0], ITSE)

    # Parametry regulatora PID
    res = sig.step(simulated_object)
    T0 = res[0][find_nearest_index(res[1], np.amax(res[1])*(0.1))]
    T = res[0][find_nearest_index(res[1], np.amax(res[1])*(0.98))] - T0
    K = res[0][-1]
    Kp = 1.2*T/(K*T0)
    Ti = 2*T0
    Td = 0.4*T0
    # Parameters of regulator
    regulator = sig.TransferFunction([Td*Ti*Kp, Ti*Kp, Kp], [Ti, 0])

    open_loop = sig.TransferFunction(np.polymul(regulator.num, simulated_object.num),  np.polymul(regulator.den, simulated_object.den))
    closed_loop = sig.TransferFunction([open_loop.num], np.polyadd(open_loop.den, open_loop.num))

    plot.figure()
    plot.title("Zieger Nichols 1")
    res = sig.step(closed_loop)
    plot.plot(res[0], res[1])
    # Odpowiedź układu z nastawami Zieger'a Nicholsa 2 szybciej się ustala przy podobnym przeregulowaniu


    plot.show()


if __name__=='__main__':
    main()

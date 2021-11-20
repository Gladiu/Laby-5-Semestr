import numpy as np
import scipy.signal as sig
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
from matplotlib import pyplot as plot

def add_transfer_functions(transfer_1, transfer_2):
    nominator = np.polyadd(np.polymul(transfer_1.num, transfer_2.den), np.polymul(transfer_2.num, transfer_1.den))
    denominator = np.polymul(transfer_1.den, transfer_2.den)
    return sig.TransferFunction(nominator, denominator)

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

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
    closed_loop = sig.TransferFunction([open_loop.den], np.polyadd(open_loop.den, open_loop.num))

    
    plot.figure()
    res = sig.step(simulated_object)
    plot.plot(res[0], res[1])
    plot.show()
    steady_state_index = np.where(res[1] == np.amax(res[1])
    steady_state_index = np.where(res[1] == np.amax(res[1])
        T =     
    T0 =     
    K =     

if __name__=='__main__':
    main()

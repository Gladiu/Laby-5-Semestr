import numpy as np
import scipy.signal as sig
from matplotlib import pyplot as plot

def add_transfer_functions(transfer_1, transfer_2):
    nominator = np.polyadd(np.polymul(transfer_1.num, transfer_2.den), np.polymul(transfer_2.num, transfer_1.den))
    denominator = np.polymul(transfer_1.den, transfer_2.den)
    return sig.TransferFunction(nominator, denominator)

def find_nearest_index(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx

def main():
    # Parametry układu
    L = 0.2
    C = 0.5
    R = 10
    
    simulated_object = sig.TransferFunction([1],[L, R, 1/C])


    plot.figure()
    plot.title("Step response of an object")
    t = np.linspace(0, 15, 1000)
    u = np.ones(len(t))
    res = sig.lsim(simulated_object, u, t)
    res = sig.step(simulated_object)
    plot.plot(res[0], res[1])
    # Parametry regulatora PID
    T0 = res[0][find_nearest_index(res[1], np.amax(res[1])*(0.1))]
    T = res[0][find_nearest_index(res[1], np.amax(res[1])*(0.98))]
    K = res[0][-1]

    Kp = 1.2*T/(K*T0)
    Ti = 2*T0
    Td = 0.4*T0
    # Parameters of regulator
    regulator = sig.TransferFunction([Td*Ti*Kp, Ti*Kp, Kp], [Ti, 0])

    open_loop = sig.TransferFunction(np.polymul(regulator.num, simulated_object.num),  np.polymul(regulator.den, simulated_object.den))
    closed_loop = sig.TransferFunction([open_loop.num], np.polyadd(open_loop.den, open_loop.num))

    plot.figure()
    plot.title("Step response of an object with PID regulator tuned with Ziegler Nichols")
    res = sig.step(closed_loop)
    plot.plot(res[0], res[1])
    # Odpowiedź takiego układu jest stabilna z minimalnym przeregulowaniem

    IAE = []
    for i in range(len(res[1])):
        if i > 0:
            IAE.append(abs(1 - res[1][i]) + IAE[i-1] )
        else:
            IAE.append(abs(1 - res[1][i]) )
    plot.figure()
    plot.title("IAE")
    plot.plot(res[0], IAE)

    plot.show()

    # Można ręcznie doprowadzać układ do mniejszej wartości błędów ręcznie zmieniając nastawy regulatora PID

if __name__=='__main__':
    main()

import numpy as np
import scipy.signal as sig
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
from matplotlib import pyplot as plot
import sympy as symbolic


L = 0.2
C = 0.5
R = 10

# Parametry regulatora PID
Tp = 2
Ti = 1
Td = 0.4
object = sig.TransferFunction(1, [L, R, 1/C])
regulator = sig.TransferFunction([Td*Ti, Ti*Tp, 0], [Ti, 0])

numerator = np.polyadd(np.polymul(object.num, regulator.den), np.polymul(object.num, regulator.den))
denominator = np.polymul(object.den, regulator.den)
openloop = sig.TransferFunction(numerator, denominator)

numerator = sig.TransferFunction(openloop.den, np.polyadd(openloop.den, openloop.num))

res = sig.step(numerator)

plot.plot(res[0], res[1])
plot.show()

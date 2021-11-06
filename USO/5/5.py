import numpy as np
import scipy.signal as sig
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
from matplotlib import pyplot as plot

# Parametry układu
L = 0.2
C = 0.5
R = 10

# Parametry regulatora PID
Kp = 2
Ti = 1
Td = 0.4

Object = sig.TransferFunction([1],[0.2, 10, 0.5])
Integrator = sig.TransferFunction([1],[Ti, 0])
Proportional = sig.TransferFunction([Kp],[1, 0])
Derivative = sig.TransferFunction([Td, 0],[1])
Integrator * Derivative

sig.TransferFunction()

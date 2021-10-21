import numpy as np 
import matplotlib.pyplot as plot
from scipy.integrate import solve_ivp
import scipy.signal as sig
import math

tf1 =  sig.TransferFunction([10], [1, 2])
tf2 =  sig.TransferFunction([4], [2, 0, 1])
tf3 =  sig.TransferFunction([-2, 6], [1, 7, 16, 12])

ss1 = sig.StateSpace(-2, 10, 1, 0)
ss2 = sig.StateSpace([[0, -1], [1, 0]], [[10],[0]], [1, 1], 0)
res = sig.step(ss1)#sig.tf2ss(10, [1,2]))

ss11 = sig.tf2ss(10, [1,2])
ss21 = sig.tf2ss(4, [2, 0, 1])
ss31 = sig.tf2ss([-2, 6], [1, 7, 16, 12])
plot.plot(res[0], res[1])
plot.show()


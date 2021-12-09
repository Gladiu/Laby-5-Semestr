# 4.1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot

kp = 2.0
T = 2.0
kob = 4
x = 1

def feedback(t,y):
    return (np.clip(kp*(x-y), -0.1, 0.1)-y)/t

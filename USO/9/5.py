import numpy as np
import scipy.signal as sig
from scipy.integrate import odeint
from matplotlib.pyplot import plot,show,title,figure,legend

# 5.1
# Punkt równowagi otrzymujemy przy wyzerowaniu wszystkich pochodnych układu
# z pierwszego równania x2 = 0 
# z trzeciego równania pierwszy składnik nam sie zeruje więc
# x3 = u/R3 
# zostało drugie równanie z którego otrzymujemy
# x1 = (g*m*R3*R3)/(km*u*u)
# podsumowując, punkt rówowagi układu uzyskujemy dla wektora
# [(g*m*R3*R3)/(km*u*u), 0, u/R3]
# podstawiając za x_1 0.1m otrzymujemy
# [ 0.1, 0, u/R3]

# 5.2
m = 0.01187
km = 1.16*10**-4
L = 0.65
R = 27.2
g = 9.81

# 5.3
u = 1

def model(x,t):
    x1 = x[1]
    x2 = g - (km*x[2]*x[2])/(m*x[0]*x[0])
    x3 = (2*km*x[1]*x[2])/(x[0]*x[0]*L) - (R*x[2])/L + u/L
    return [x1, x2, x3]

# 5.4
t = np.linspace(0, 5, 100)
res = odeint(model, [0.1, 0, u/R], t)
figure()
plot(t, res[:,0])
plot(t, res[:,1])
plot(t, res[:,2])
show()

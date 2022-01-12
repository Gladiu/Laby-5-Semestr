import numpy as np
import scipy.signal as sig
from scipy.integrate import odeint
from matplotlib.pyplot import plot,show,title,figure

# 2.1
l = 1 
m = 9 
J = 1 
d = 0.5
g = 9.81

#theta' = x2
#theta'' = -d*x2/J - m*g*l*sin(x1)/J + u 

# 2.2
def model(x,t):
    x1 = x[1]
    x2 = -(d*x[1])/J - (m*g*l*np.sin(x[0]))/J +  0
    return [x1,x2]

t = np.linspace(0, 5,100)
res = odeint(model,[np.pi/4, 0],t)
figure()
title("Niezlinearyzowany model")
plot(t, res[:,0])
plot(t, res[:,1])

# 2.3

#theta' = x2
#theta'' = -d*x2/J - m*g*l*sin(x1)/J + u 

#df1/dx1 = 0
#df2/dx1 = -m*g*l*cos(x1)/J
#df1/dx2 = 1
#df2/dx2 = -d/J
#df1/du = 0
#df2/du = 1

# Dla punktu [pi, 0] podstawiam wartości

A = np.array([[0, 1],[(m*g*l)/J, -d/J]])
B = np.array([[0],[1]])

show()

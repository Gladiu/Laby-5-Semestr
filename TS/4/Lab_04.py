# -*- coding: utf-8 -*-
"""
@author: Radoslaw Patelski
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal



Zadanie_2 = False
Zadanie_3 = True
Zadanie_4 = False
Zadanie_5 = False
#initialize constant values
b = 0.5
k = 1
m = 1

#set time step and calculate vector of timestamps
Tp = 0.1
Tf = 10
samples = int(Tf/Tp + 1)

T = np.linspace(0,Tf,samples)

if Zadanie_2 or Zadanie_3:
    #prepare all input signals - control U and noised W and V
    U = np.full(samples, 1)
    W = np.random.normal(0,1,samples)
    V = np.array([np.random.normal(0,0,samples),np.random.normal(0,0,samples)]) #for now assume no process noise V (model is perfect)
if Zadanie_4:
    #prepare all input signals - control U and noised W and V
    U = np.full(samples, 1)
    W = np.random.normal(0,1,samples)
    V = np.array([np.random.normal(0,0,samples),np.random.normal(0,0,samples)]) #for now assume no process noise V (model is perfect)

#define arrays A, B and C and D of a linear system
A = np.array([[0, 1],
              [-k/m, -b/m]])

B = np.array([[0],
              [1/m]])

C = np.array([[1, 0]])

D = np.array([[0]])

#modify signals to include noise
B0 = np.array([[1, 0],
              [0, 1]])

U0 = np.array([V[0],
               V[1] + 1/m * U])

D0 = np.array([[0, 0]])



#simulate the dynamic system, pass matrices of linear system model, control signal and timestamps
res = signal.lsim([A,B0,C,D0],U0.T,T)
X = res[2]
Y = res[1]

#plot states of dynamic system
plt.figure()
plt.plot(T, X)
plt.title("Real plant")
plt.grid()

#add noise to the measurement
Y = Y + W

plt.figure()
plt.plot(T,Y)
plt.title("Noised measurement")
plt.grid()


#calculate matrices A, B, C and D of discrete-time system based on continous system

#
# TODO
#

A = (A*Tp + np.eye(2))
B = B*Tp

if Zadanie_2:
    #initialize all matrices of Kalman Filter - feel free to change these values  
    Xc = np.array([[0],[0]]) #Xc (a posteriori estimate X) - assumed initial conditions
    Pc = np.array([[0,0],[0,0]]) #Pc (a posteriori P) - how unsure we are of initial conditions
    #a priori estiamtes Xp and Pp are not initialized, as they will be calculated based on a posteriori values and measured signals

    Q = np.array([[0,0],[0,0]]) #Q - assumed covariance of process noise
    R = np.cov(W) #R - assumed covariance of measurement noise
if Zadanie_3:
    #initialize all matrices of Kalman Filter - feel free to change these values  
    Xc = np.array([[3],[-1]]) #Xc (a posteriori estimate X) - assumed initial conditions
    Pc = np.array([[3, 0],[0,-1]]) #Pc (a posteriori P) - how unsure we are of initial conditions
    #a priori estiamtes Xp and Pp are not initialized, as they will be calculated based on a posteriori values and measured signals

    Q = np.array([[2.5,0.125],[.5, 0.125]]) * 0.1 #Q - assumed covariance of process noise
    R = 100 #R - assumed covariance of measurement noise

#some vectors to keep samples of Xc aposteriori and Xp apriori estimate for later plotting
XC = Xc.T
XP = Xc.T


#main loop of discrete-time simulation
for n in range(0,samples - 1):  
    # Kalman filter
    if Zadanie_2 or Zadanie_3:
        # A priori
        Xp = A @ Xc + B * U[n]
        Pp = A @ Pc @ A.T + Q 
        # A posteriori
        e = Y[n] - C @ Xp
        S = C @ Pp @ C.T + R
        K = Pp @ C.T @ np.linalg.inv(S)
        Pc = Pp - K @ S @ K.T
        Xc = Xp + K @ e

        # Add calculated values to XC and XP 
        XC = np.vstack([XC, Xc.T])
        XP = np.vstack([XP, Xp.T])
    if Zadanie_4:
        # A priori
        Xp = A @ Xc + B * U[n]
        Pp = A @ Pc @ A.T + Q 
        # A posteriori
        e = Y[n] - C @ Xp
        S = C @ Pp @ C.T + R
        K = Pp @ C.T @ np.linalg.inv(S)
        Pc = Pp - K @ S @ K.T
        Xc = Xp + K @ e

        # Add calculated values to XC and XP 
        XC = np.vstack([XC, Xc.T])
        XP = np.vstack([XP, Xp.T])


#plot the results
plt.figure()
plt.plot(T, XP)
plt.title("Apriori estimate")
plt.grid()

plt.figure()
plt.plot(T, XC)
plt.title("Aposteriori estimate")
plt.grid()

plt.figure()
plt.plot(T, X - XC)
plt.title("Estimation errors")
plt.grid()

plt.show()

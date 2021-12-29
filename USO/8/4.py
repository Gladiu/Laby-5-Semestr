# 4.1
import numpy as np
from scipy.integrate import odeint
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
from matplotlib.pyplot import figure
from matplotlib.pyplot import title

kp = 2.0
T = 2.0
kob = 4
force = 1

# 4.2
def feedback(x,t):
    u = np.clip(kp*(force-x), -0.1, 0.1) 
    x_next = -x + u*kob
    return x_next

t = np.linspace(0, 5, 100)

# 4.3
res = odeint(feedback, [0],t)

# Wykreślanie odpowiedzi będzie później razem z innymi wymuszeniami
#plot(t, res[:,0])

# 4.4
for force in [1,2,3]:

    def feedback_in_loop(x,t):
        u = np.clip(kp*(force-x), -0.1, 0.1) 
        x_next = -x + u*kob
        return x_next
    figure()
    title("Odpowiedź na wymuszenie = "+str(force))
    res = odeint(feedback_in_loop, [0],t)
    plot(t, res[:,0])
# Nie jest zachowana zasada superpozycji a układ nie jest liniowy przez dodanie ograniczenia
# sygnału wymuszającego

# 4.5
for force in [1,2,3]:

    def feedback_in_loop(x,t):
        u = kp*(force-x)
        x_next = -x + u*kob
        return x_next
    figure()
    title("Odpowiedź na wymuszenie bez ograniczenia = "+str(force))
    res = odeint(feedback_in_loop, [0],t)
    plot(t, res[:,0])

# Zasada superpozycji jest zachowana a układ jest liniowy po usunięciu saturacji
show()

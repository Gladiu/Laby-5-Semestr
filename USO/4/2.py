import numpy as np 
import scipy
from scipy import optimize
import matplotlib.pyplot as plot

# Zadanie 2.1
# -y -> max
# ogr.
# 2x-y <=  4
# y+x  >   3
# y+4x >= -2
#
# y >= -4+2x
# y > 3-x
# y >= -2-4x
#
# 0 >= -4+2x-y
# 0 > 3-x-y
# 0 >= -2-4x - y

x = np.linspace(-10, 10, 100)

y = -x
y1 = x*2-4
y2 = -x+3
y3 = -x*4-2

plot.fill_between(x, y2, y1, alpha=0.5)
plot.fill_between(x, y3, y2, alpha=0.5)
plot.plot(x, y)

def fun(arguments):
    x, y = arguments
    return -y
# Zadanie optymalizacji
# Z wykresu odczytać można 0.3 -3.3

# Define constraints
cons = ({'type': 'ineq', 'fun': lambda x:  2*x[0] - x[1] - 4 },
        {'type': 'ineq', 'fun': lambda x: -x[0] - x[1] + 3},
        {'type': 'ineq', 'fun': lambda x: -4*x[0] - x[1] - 2})

# Use actual function
res = scipy.optimize.minimize(fun, [0.3, 3.3], method='SLSQP', constraints=cons)
print(res)


plot.show()

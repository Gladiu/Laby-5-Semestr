import numpy as np 
import scipy as sci
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

x = np.linspace(-10, 10, 100)

y = -x
y1 = x*2-4
y2 = -x+3
y3 = -x*4-2

plot.fill_between(x, y2, y1, alpha=0.5)
plot.fill_between(x, y3, y2, alpha=0.5)
plot.plot(x, y)

# Zadanie optymalizacji

# Define constraints


plot.show()

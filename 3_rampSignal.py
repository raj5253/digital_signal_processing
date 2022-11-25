from cgitb import small
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

x = np.arange(-5, 10, 1)


def func(m, c, x):
    li = []
    for sample in x:
        if sample <= 0:
            li.append(0)
        else:
            li.append(m * sample + c)
    return li


y = func(2, 0, x)   # if signal need to pass from origin then c should be 0

plt.stem(x, y)

plt.xticks(x)
plt.yticks([0, 1])
plt.xlabel("time")
plt.ylabel("Amplitute")
plt.title("Ramp singal")
plt.show()

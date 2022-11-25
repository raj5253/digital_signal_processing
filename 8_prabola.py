
import math as mt
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

x = np.arange(-15, 16, 1)
# x = range(0, 20, 1)


def func(x, a):
    li = []
    for sample in x:
        value = a * sample * sample
        li.append(value)
    return li


y = func(x, 4)   # if signal need to pass from origin then c should be 0

plt.stem(x, y)
# plt.plot(x, y)

plt.xticks(x)

plt.xlabel("time")
plt.ylabel("Amplitute")
plt.title("parabolic Signal")
plt.show()

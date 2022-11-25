
import math as mt
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

x = np.arange(0, 10, .5)
# x = range(0, 20, 1)


def func(x, w):
    li = []
    for sample in x:
        value = mt.cos(sample * w)
        li.append(value)
    return li


y = func(x, 0.5)  

plt.stem(x, y)
# plt.plot(x, y)

plt.xticks(x)

plt.xlabel("time")
plt.ylabel("Amplitute")
plt.title("cos(wt), w = 0.5")
plt.show()

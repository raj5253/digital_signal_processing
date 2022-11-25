
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
        value = mt.sin(sample * w)
        li.append(value)
    return li


y = func(x, 2)  

plt.stem(x, y)
# plt.plot(x, y)

plt.xticks(x)

plt.xlabel("time")
plt.ylabel("Amplitute")
plt.title("sin(wt), w = 2")
plt.show()

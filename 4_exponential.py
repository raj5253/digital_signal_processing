from cgitb import small
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

x = np.arange(-2, 2, 0.1)


def func(m, x):
    li = []
    for sample in x:
        if sample <= 0:
            li.append(0)
        else:
            li.append(np.exp(sample * m))
    return li


y = func(2, x)   # if signal need to pass from origin then c should be 0

plt.stem(x, y)

# plt.xticks(x)
# plt.yticks(y)        # y limits will not be 1
plt.xlabel("time")
plt.ylabel("Amplitute")
plt.title("Exponential signal for a = 4")
plt.show()

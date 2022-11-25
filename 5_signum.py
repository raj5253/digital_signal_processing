from cgitb import small
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

# x = np.arange(-5, 10,.1)
x1 = np.arange(-5, 10, 1)


def func(x):
    li = []
    for sample in x:
        if sample < 0:
            li.append(-1)
        elif sample == 0:
            li.append(0)
        else:
            li.append(1)
    return li


y = func(x1)

plt.stem(x1, y)
# plt.plot(x, y)

plt.xticks(x1)
# plt.yticks([0, 1])
plt.xlabel("time")
plt.ylabel("Amplitute")
plt.title("signum sginal")
plt.show()

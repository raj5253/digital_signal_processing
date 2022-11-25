import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

x = np.arange(-5, 10, 1)


def func(a, x):
    li = []
    for sample in x:
        if sample < a:
            li.append(0)
        else:
            li.append(1)
    return li


y = func(4, x)

plt.stem(x, y)

plt.xticks(x)
plt.yticks([0, 1])
plt.xlabel("time")
plt.ylabel("Amplitute")
plt.title("Unit step signal for a = 4")
plt.show()

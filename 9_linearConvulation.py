
import math as mt
import numpy as np
import matplotlib.pyplot as plt


x = [4, 6, 2, 6, 1, 9, 8, 1, 7]             # input- 5
h = [5, 1, 6, 1]           # impulse - 6

N1 = len(x)
N2 = len(h)
N = N1 + N2 - 1


y = np.zeros(N)           # create an array of zeroes of size N

y1 = np.convolve(x, h)
m = N - N1
n = N - N2

x = np.pad(x, (0, m), 'constant')
print(x)
h = np.pad(h, (0, n), 'constant')
print(h)


for n in range(N):
    for k in range(N):
        if k <= n:             # each daigonal comes from a small square mtx of the whole matrix.
            # if row index increase then column index should decrease for maintaing in the daigonal path of smaller matrix.
            y[n] = y[n] + x[n-k] * h[k]


xaxis = range(N)
plt.stem(xaxis, y)

print(y1)
print(y)

plt.xticks(xaxis)
plt.yticks(y1)

plt.xlabel("time")
plt.ylabel("Amplitute")
plt.title("linear convulation")
plt.show()

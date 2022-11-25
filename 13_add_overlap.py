import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

x = list(map(int, input("Enter the input signal: x: ").split()))  # sig
h = list(map(int, input("Enter the filter signal : h: ").split()))  # filt
n = int(input("Enter the length of block: n: "))

x_len = len(x)
h_len = len(h)


print(x)  # [2, -2, 8, -2, -2, -3, -2, 1, -1, 9, 1, 3]
print(h)  # [1, -2, 3]


# fsig #[  2.  -6.  18. -24.  26.  -5.  -2.  -4.  -9.  14. -20.  28.  -3.   9.]
list1 = signal.oaconvolve(x, h)

fig, (first, second) = plt.subplots(2, 1)  # fig = figure_name


print("The covolution of the sequnce is : ",  list1)
first.stem(x)
# first.plot(x)
first.set_title("orignal signal")  # sig
second.stem(list1)
# second.plot(list1)
second.set_title("filtered signal")  # fsig


# plt.xticks(Input)
# plt.yticks(list1[0:x_len])
# plt.xticks(inlist)
# plt.yticks(list1)

fig.tight_layout()
fig.show()

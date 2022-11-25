import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

x = list(map(int, input("Enter the input signal: x: ").split()))  # sig
h = list(map(int, input("Enter the filter signal : h: ").split()))  # filt
n = int(input("Enter the length of block: n: "))


def circular_conv(x, h):
    y = np.convolve(x, h)
    n = len(y)
    k = max(len(x), len(h))
    for i in range(n - k):
        y[i] += y[k+i]
    output = y[:k]
    return output


x_len = len(x)
h_len = len(h)
M = h_len
N = n

L = N - (M - 1)

# %L  # divide the whole x into L sized blocks. pad if reqired to achieve L size
rem = x_len % M
if rem != 0:
    for i in range(L-rem):
        x.append(0)

if L != 0:  # you can go without conditional also. just N > M-1
    x_list = [x[i:i+L] for i in range(0, x_len, L)]  # L size interval

for i in x_list:
    for j in range(M-1):  # append M-1 zeroes to each of the block
        i.append(0)

print("Fregmented blocks: ", x_list)

res1 = []
for li in x_list:
    out = circular_conv(li, h)
    res1.append(out)       # append the circluar conv of each block


print("Circular convolve: ", res1)
no_of_block = len(res1)

# Block size = N
# now overlapp add them.
final_res = list(res1[0])

for i in range(1, len(res1)):
    fl = len(final_res)
    for j in range(N):
        if j < M-1:
            final_res[fl - (M-1) + j] += res1[i][j]
        else:
            final_res.append(res1[i][j])

print("FT: ", final_res)

# 2  -2  8  -2  -2  -3  -2  1  -1  9  1  3
#  1 -2 3

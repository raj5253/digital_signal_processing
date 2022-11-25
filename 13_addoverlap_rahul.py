import numpy as np
import matplotlib.pyplot as plt

x = list(map(int, input("Enter the sequence x{n}: ").split()))
h = list(map(int, input("Enter the sequence x{n}: ").split()))

res = np.convolve(x, h)

l = len(x)
m = len(h)

n = int(l / m)
p = l % m

if p != 0:
    for i in range(m - p):
        x.append(0)

li = [x[i:i + m] for i in range(0, l, m)]

res1 = []
print(li)
for i in range(len(li)):
    temp = np.convolve(li[i], h)
    res1.append(list(temp))
p = len(res1[1])
print(res1)
# print(p)
final_res = res1[0]
for i in range(1, len(res1)):
    for j in range(p):
        len_fin_res = len(final_res)
        if j < m-1:
            final_res[len_fin_res-m+1+j] += res1[i][j]
        else:
            final_res.append(res1[i][j])
print(final_res)

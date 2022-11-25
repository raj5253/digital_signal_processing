from pickletools import read_int4
import numpy as np
import matplotlib.pyplot as plt


x = list(map(int, input("Enter the 1st sequence ").split()))

h = list(map(int, input("Enter the 2nd sequence ").split()))
x_len = len(x)
h_len = len(h)

print(x)
print(h)

if x_len > h_len:
    for i in range(x_len-h_len):
        h.append(0)
    print(f"second sequence is {h}")
    h_len = len(h)
if x_len < h_len:
    for i in range(h_len-x_len):
        x.append(0)
    print(f"First Sequence is {x}")
    x_len = len(x)


list1 = np.convolve(x, h)
print(list1)

total = len(list1)
Input = range(x_len)
for i in range(abs(x_len - total)):
    # total-x_len = x_len 😂. go for  10_circonvolution.py
    list1[i] += list1[total-x_len+1+i]
print(f"The covolution of the sequnce is {list1[:x_len]}")
plt.stem(Input, list1[0:x_len])

plt.xticks(Input)
plt.yticks(list1[0:x_len])
plt.show()

# 4 6 2 6 1 9 8 1 7 #5 1 6 1

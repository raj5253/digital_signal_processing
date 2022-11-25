import numpy as np
import matplotlib.pyplot as plt


x = list(map(int, input("Enter the 1st sequence ").split()))

h = list(reversed(x))

x_len = len(x)
h_len = len(h)


print(x)
print(h)


list1 = np.convolve(x, h)
print(list1)

# total = len(list1)
# Input = range(total)

n = x_len

inlist = []
for i in range(n):  # appending the index in reverse fashion
    inlist.append(-(n-1 - i))

inlist.remove(0)

for i in range(h_len):
    inlist.append(i)

print("The covolution of the sequnce is : ",  list1)
# plt.stem(Input, list1)
plt.stem(inlist, list1)


plt.xticks(inlist)
plt.yticks(list1)
plt.show()

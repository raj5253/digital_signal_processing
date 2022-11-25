import numpy as np
import matplotlib.pyplot as plt
import scipy as sc


x = list(map(int, input("Enter the 1st sequence : x: ").split()))
h = list(map(int, input("Enter the 2nd sequence : h: ").split()))

h1 = h
h = list(reversed(h))

x_len = len(x)
h_len = len(h)


print(x)
print(h)


list1 = np.convolve(x, h)
# list1 = sc.signal.correlate(x, h, mode= "full")  #this can also work.
# list1 = np.correlate(x,h1, mode="full")  #this can also work.

# total = len(list1)
# Input = range(total)

n = x_len

inlist = []
for i in range(n):  # appending the reverse count
    inlist.append(-(n-1 - i))

inlist.remove(0)

for i in range(h_len):
    inlist.append(i)

print("The covolution of the sequnce is : ",  list1)
plt.stem(inlist, list1)

plt.xticks(inlist)
plt.yticks(list1)
plt.show()

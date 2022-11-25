import numpy as np
import matplotlib.pyplot as plt

x = list(map(int, input("Enter x series : ").split()))
h = list(map(int, input("Enter h series : ").split()))

n1 = len(x)
n2 = len(h)

n = n1 + n2 - 1

remx = n - n1
remh = n - n2

x = np.pad(x, (0, remx), 'constant')
h = np.pad(h, (0, remh), 'constant')

output = np.zeros(n)

for i in range(n):
    for k in range(n):
        if k <= i:
            output[i] = output[i] + x[i-k] * h[k]

# y is linear convoultin

k = max(n1, n2)
# x_len = k
# total = n
print(k, n)

print(output)
# offshoot = n - k
for i in range(n - k):
    # reach the position from where clipping need to be started. thats it
    output[i] += output[k + i]


print(output)

plt.stem(range(k), output[0: k])
plt.xticks(range(k))
plt.yticks(output[0: k])
plt.show()


# 4 6 2 6 1 9 8 1 7
#  5 1 6 1

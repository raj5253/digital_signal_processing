import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import cmath

x = list(map(int, input("Enter the input signal: x: ").split()))  # sig

x_len = len(x)

in_time_list = []
for i in range(x_len):
    in_time_list.append(i)

N = x_len
k_list = []

output_list = np.fft.fft(x)

for k in range(N):
    temp = 0
    for i in range(N):
        temp += (x[i] * complex(np.cos(2 * np.pi * k * i / N), -
                 np.sin(2 * np.pi * k * i / N)))
    k_list.append(temp)

k_list = np.array(k_list)

magn_list = []
for i in k_list:
    magn_list.append(abs(i))


phase_list = []
for i in k_list:
    phase_list.append(cmath.phase(i) * 180 / np.pi)
print("Input : ", x)
print("D F T : ", output_list)
print("D F T : ", k_list)

# plt.stem(in_time_list, output_list)
# plt.show()

plt.stem(in_time_list, magn_list)
plt.show()

plt.stem(in_time_list, phase_list)
plt.yticks(phase_list)
plt.show()

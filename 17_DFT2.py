from cmath import phase
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import cmath
import math

x = list(map(int, input("Enter the input signal: x: ").split()))  # sig

x_len = len(x)

in_time_list = []
for i in range(x_len):
    in_time_list.append(i)

output_list = np.fft.fft(x)

phase_list = []
for i in output_list:
    phase_list.append(math.degrees(cmath.phase(i)))   # in degrees

print("Input : ", x)
print("D F T : ", output_list)
print("Phase : ", phase_list)


fig, (first, second) = plt.subplots(2, 1)  # fig = figure_name

first.stem(in_time_list, output_list)
first.set_yticks(output_list)
first.set_title("Magnitude plot")


second.stem(in_time_list, phase_list)
second.set_yticks(phase_list)
second.set_title("Phase plot")


plt.show()


# x = list(map(int, input("Enter the sequence x[n] : ").split()))
# N = len(x)
# li = []
# for i in range(N):
#     li.append([])
#     for j in range(N):
#         val = complex(math.cos((2*math.pi*j*i)/N), -
#                       math.sin((2*math.pi*j*i)/N))
#         li[i].append(val)

# ans = []
# for i in range(N):
#     sum = 0
#     for j in range(N):
#         sum += li[i][j]*x[j]
#     ans.append(sum)
# ans = np.array(ans)
# plt.subplot(2, 1, 1)
# plt.xticks(range(N))
# plt.yticks((abs(ans)))
# plt.xlabel("   Freq(Hz)   ")
# plt.ylabel("  Magnitude -->  ")
# plt.stem(range(N), abs(ans))
# plt.subplot(2, 1, 2)
# plt.xticks(range(N))
# plt.yticks(np.angle(ans, deg=True))
# plt.xlabel("   Freq(Hz)    ")
# plt.ylabel("  phase-->  ")
# plt.stem(range(N), np.angle(ans, deg=True))
# plt.savefig('DFT.png')
# plt.show()

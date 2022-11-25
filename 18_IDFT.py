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

inverse_list = np.fft.ifft(output_list)

phase_list = []
for i in output_list:
    phase_list.append(math.degrees(cmath.phase(i)))   # in degrees

print("Input : ", x)
print("D F T : ", output_list)
print("I D F T : ", inverse_list)
print("Phase : ", phase_list)


fig, (first, second, third) = plt.subplots(
    3, 1, sharex=True)  # fig = figure_name
fig.subplots_adjust(wspace=0.5, hspace=0.5)

first.stem(in_time_list, output_list)
first.set_yticks(output_list)
first.set_title("Magnitude -DFT")


second.stem(in_time_list, phase_list)
second.set_yticks(phase_list)
second.set_title("Phase plot")

third.stem(in_time_list, inverse_list)
third.set_yticks(inverse_list)
third.set_title("IDFT")


plt.show()
# input : 1 2 0 3
# this was solved in class by vamshi sir.

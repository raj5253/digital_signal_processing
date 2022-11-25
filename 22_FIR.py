import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# fc = np.array([100, 200])
Fs = 9000
fp = 1500
fs = 2000

wp = 2 * fp/Fs
ws = 2 * fs/Fs

# b = signal.firwin(31, wp, pass_zero='highpass')
# b = signal.firwin(31, wp, pass_zero='lowpass')
# b = signal.firwin(31, [wp, ws], pass_zero='bandpass')
b = signal.firwin(31, [wp, ws], pass_zero='bandstop')

[w, h] = signal.freqz(b,  worN=2000)

freq = Fs * w / (2 * np.pi)

amplitude = 20 * np.log10(abs(h))

angle = np.angle(h) * 180/np.pi

plt.plot(w/np.pi, amplitude)
plt.xlabel("freq-Normalised")
plt.ylabel("Gain in dB")
plt.show()

plt.plot(w/np.pi, angle)
plt.xlabel("freq-Normalised")
plt.ylabel("Phase in degrees")
plt.show()

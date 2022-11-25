import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
import cmath


Fs = 7000  # sampling rate
fp = 1500  # passbandfreq
fs = 3000  # stopband freq
rp = 0.15  # passband ripple maximum loss
rs = 60  # stopband ripple minimum attenuation

# Fs = 7500  # sampling rate  # for
# fp = 900  # passbandfreq
# fs = 1300  # stopband freq
# rp = 0.29  # passband ripple maximum loss
# rs = 29  # stopband ripple minimum attenuation

wp = 2*fp/Fs  # normalised-start ang_fre
ws = 2*fs/Fs  # normalised-stop ang_freq

[n, wn] = sc.cheb1ord(wp, ws, rp, rs, 's')
print(wn)  # wn = cutoff_angular_freq(normalised)

# [z, p, k] = sc.cheby1(n, 3, wn, btype='lowpass', analog=True, output='zpk')
# [z, p, k] = sc.cheby1(n, 3,  wn, btype='highpass',analog=True, output='zpk')  # ripple = 3
# [z, p, k] = sc.cheby1(n,3, [wp, ws], btype='bandpass', analog=True, output='zpk')
[z, p, k] = sc.cheby1(n, 3, [wp, ws], btype='bandstop',
                      analog=True, output='zpk')

[b, a] = sc.zpk2tf(z, p, k)
# [b, a] = sc.butter(n, wp, 'low', analog=True, output='ba')
wor = np.arange(0, np.pi, .01)
[w, h] = sc.freqs(b, a, wor)
# print(w, h)  # h= output array of impulse response(a complex) and, w = ouput array of angular_freq(normalized)


freq = Fs*w/(2*np.pi)  # freq in hz(non-normalised)

h_db = 20*np.log10(abs(h))  # aplitude-dBs
an = np.angle(h)
# plt.figure(1)
plt.xlabel('Frequency normalised')
plt.ylabel(' Gain in dB')
plt.grid('on')
# plt.plot(w/np.pi, h_db)
plt.plot(w/np.pi,  h_db)

plt.show()
# plt.figure(2)
plt.xlabel('Normalized Frequency')
plt.ylabel('Phase in radians')
plt.grid('on')
plt.plot(w/np.pi, an)
plt.show()

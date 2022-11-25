import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# import scipy as sc


x = list(map(int, input("Enter the input signal: x: ").split()))  # sig
h = list(map(int, input("Enter the filter signal : h: ").split()))  # filt

b, a = signal.cheby1(4, 5, 100, 'lowpass', analog=True)

w, h = signal.freqs(b, a)
plt.semilogx(w, np.log10(abs(h)))

plt.title(f"Chebyshev frequency response  rp={5}")
plt.xlabel("Angular frequnecy( rad/sec)")
plt.ylabel("Amplitude[dB]")

plt.axvline(100, color='green')  # cutoff frequency


# """ signal.fliters(numernator_series, denominator_series) ::  Compute frequency response of analog filter.
# returns :
#     w : ndarray
#         The angular frequencies at which `h` was computed.
#     h : ndarray
#         The frequency response.
#     so,w = angular_freq, h= freq,  we get amplitude from h
# """

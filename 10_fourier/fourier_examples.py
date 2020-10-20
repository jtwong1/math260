# Examples:
#   - construct a signal as a Fourier series
#   - compute the fft in numpy and plot real/imag parts
#   - comparison of shifted/non-shifted frequencies
#
#   * note that fftshift only moves the data in the array (the shift);
#   while fftfreq creates the symmetric -n/2 to n/2 range of frequencies.
#   * note that fftfreq(n,d) returns
#       [0, 1, 2, ... n//2, -n//2+1, ..., -1]/(n*d)
#
#   which gives the frequencies in cycles/time.

import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin
from numpy import fft


def signal_sines(t, m=50):
    """ A signal with ~1/k sized amplitude, sine terms with
        `every other' frequency in the Fourier series.
         (with t in seconds, these are 1, 3, 5... cycles/s)
    """
    total = 0
    for k in range(1, m):
        total += 1/k*sin(2*pi*(2*k-1)*t)
    return total


def example(n, length=1):
    """ Use of the numpy.fft package: plot the DFT of the example signal.
        Inputs:
            n - number of sample points
            length - the duration of the sample interval
            signal - a function f(t) to sample

        Note that non-shifted and shifted versions are computed here.
    """
    t = np.linspace(0, length, n, endpoint=False)  # times, in `seconds'
    d = t[1] - t[0]  # sample spacing
    s = [signal_sines(tt) for tt in t]  # signal (samples)

    # take the FFT (including 1/n) and get frequencies (cycles/unit of time)
    # now freqs line up with F correctly...
    freq = fft.fftfreq(n, d)  # freq = [0, 1, ... n/2, -n/2+1, ..., -1]/length
    sf = fft.fft(s)/n

    # plot the DFT, real/imag parts
    # ...freqs are *not* in increasing order, but the plot doesn't care
    dualplot(freq, sf, "DFT (real/imag parts)")
    plt.show()

    # shifted freqs/transform: freq_centered = [-n/2+1, ... -1,0,1, ... , n/2]
    freq_centered = fft.fftshift(freq)  # freqs are increasing; freq[n//2] = 0
    sf_centered = fft.fftshift(sf)


def freq_plot(n):
    """ Example: plotting the frequencies and shifted versions vs. index """
    d = 1/n  # sample spacing (assuming n samples in [0, 1])
    freq = fft.fftfreq(n, d)  # frequencies [0, 1, ... n/2, -n/2+1, ..., -1]
    freq_centered = fft.fftshift(freq)  # shifted: [-n/2+1,...-1,0,1, ..., n/2]
    ind = range(len(freq_centered))

    plt.figure(figsize=(4, 3))
    plt.plot(ind, freq, '.k', ind, freq_centered, '.r')
    plt.legend(['no shift', 'shift'])
    plt.xlabel('index')
    plt.ylabel('freq')
    plt.show()

    return freq


def dualplot(freq, sf, name):
    """ simple plot of real and imaginary parts """
    plt.figure(figsize=(6.5, 2.5))
    plt.suptitle(name)
    plt.subplot(1, 2, 1)
    plt.plot(freq, np.real(sf), '.k')
    plt.ylabel('Re(F)')
    plt.subplot(1, 2, 2)
    plt.plot(freq, np.imag(sf), '.k')
    plt.ylabel('Im(F)')
    plt.subplots_adjust(wspace=0.5)

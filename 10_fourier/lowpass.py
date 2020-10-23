""" low pass filter example (wav file required).
    Run test_sound(cutoff, name) to generated filtered sound. """

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq
from scipy.io import wavfile


def low_pass(rate, data, length, cutoff):
    """ basic low pass filter for data
        Arguments:
            rate - the sample rate (Hz) (wav default: 44100 Hz)
            data - the samples
            length - the length (s) of the sample window
            cutoff - remove frequencies above this value
        Returns:
            filtered - the filtered data
    """
    n = data.shape[0]
    freq = fftfreq(n, 1/rate)  # freqs in Hz, (0 ... n/2-1, -n/2, .. -1)/L
    df = fft(data)/n

    # find index for cutoff freq.
    # then cut off frequences k+1 to n/2 and -n/2 to -(k+1)
    k = np.searchsorted(freq[0:n//2], cutoff)
    df[k+1:n//2] = 0
    df[n//2:-k] = 0

    filtered = n*ifft(df)
    return filtered


def test_filter_on_wav(cutoff, fname):
    """ Example to illustrate the low-pass filter on a sound wave.
        Writes the filtered sound to a new .wave file
        Shows some extra information:
            - check that the ifft of the filtered signal is real
            - plot of magnitude of spectrum for the original/filtered signal
        Inputs:
            cutoff - Hz; remove frequencies about this value
            fname - filename (must be a .wav file)

        NOTE: for simplicity, only keeps the *left channel* of the .wav file
            if it is a stereo audio file.
    """
    # load the wav file, remove right channel if applicable
    rate, data = wavfile.read(fname)
    length = data.shape[0] / rate
    if data.shape[1] > 1:
        data = data[:, 0]  # keep only the left channel

    filtered = low_pass(rate, data, length, cutoff)

    # check that the ifft is real (it should be if cutoff was done right!)
    plt.plot(np.imag(filtered[::100]), '.b')
    plt.title("imag. part of filtered wave")
    imag_size = np.max(np.abs(np.imag(filtered)))
    print(f"Max imag. part: {imag_size:.3e}")

    # now remove the (small) imaginary part from rounding error
    filtered = np.real(filtered)

    # write the filtered wave to a file
    # NOTE: complex ifft returns an array of complex numbers,
    # but the wav type is an array of *ints*; fix with .astype()
    filename = "filtered_{:.0f}.wav".format(cutoff)
    wavfile.write(filename, rate, filtered.astype(data.dtype))

    # plot the spectra for the two signals for comparison
    plt.figure(figsize=(7, 3))
    plt.subplot(1, 2, 1)
    plot_spectrum(data, rate, plotname="original")
    plt.subplot(1, 2, 2)
    plot_spectrum(filtered, rate, plotname=f"cut={cutoff:.0f}")
    plt.subplots_adjust(wspace=0.5)
    plt.show()
    plt.savefig(f'wav_{cutoff:.0f}.pdf', bbox_inches='tight')


def plot_spectrum(data, rate, plotname):
    """ plots the log(|F|) for the DFT F vs. frequency (0 to n/2)
        on a semilog x plot. Note that log(magnitude) is proportional
        to decibels, the familiar measure for sound volume here.
    """
    n = data.shape[0]

    transform = fft(data)/n
    log_magnitude = np.log(np.abs(transform))
    freq = fftfreq(n, 1/rate)
    skip = round(freq.shape[0]/2048)  # thin out the plot
    plt.semilogx(freq[:n//2:skip], log_magnitude[:n//2:skip])
    plt.xlabel('freq (Hz)')
    plt.ylabel('log(|F|)')
    plt.title(plotname)


if __name__ == "__main__":
    # low-pass filter on a wave, with two different cutoffs (in Hz)
    test_filter_on_wav(1200, "roar.wav")
    test_filter_on_wav(2000, "roar.wav")

""" Example code: touch tone exercise. Simple solution to select tones. """

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft
from scipy.io import wavfile


def tone_data():
    """ Builds the data for the phone number sounds
        Returns:
            tones - list of the freqs. present in the phone number sounds
            nums - a dictionary mapping the num. k to its two freqs.
            pairs - a dictionary mapping the two freqs. to the nums

        For example, 4 is represented by the two freqs 697 (low), 1336 (high)
        and nums[4] = (697, 1336)

        `pairs' maps the opposite way: pairs[(697, 1336)] = 4
    """
    lows = [697, 770, 852, 941]
    highs = [1209, 1336, 1477, 1633]  # (Hz)

    nums = {}
    for k in range(0, 3):
        nums[k+1] = (lows[k], highs[0])
        nums[k+4] = (lows[k], highs[1])
        nums[k+7] = (lows[k], highs[2])
    nums[0] = (lows[1], highs[3])

    pairs = {}
    for k, v in nums.items():
        pairs[(v[0], v[1])] = k

    return lows + highs, nums, pairs


def load_wav(fname):
    """ Loads a .wav file, returning the sound data.
        NOTE: rerns an Nxk array, where k = number of channels.
        (mono -> 1, stereo -> 2, etc.)

        Returns:
            rate - the sample rate (in samples/sec)
            data - an Nx1 (left/right) or Nx2 (stereo) np.array
                   of the samples.
            length - the duration of the sound (sec)
    """
    rate, data = wavfile.read(fname)
    if len(data.shape) > 1 and data.shape[1] > 1:
        print(f".wave file in stereo: returning {data.shape[1]} channels")
    length = data.shape[0] / rate
    print(f"Loaded sound file {fname}.")
    return rate, data, length


def extract_tone(freqs, df):
    """ extracts the specified frequencies from the fft,
        given the scaled but not shifted freqs/df """
    ex = []

    n = df.shape[0]
    mag = np.abs(df[0:n//2])  # only need the first half
    peak = max(mag)
    thresh = 0.2

    tones = tone_data()[0]

    w = int(50/(freqs[1] - freqs[0]))
    pos = 0
    for tone in tones:
        while freqs[pos] < tone:
            pos += 1
        local_peak = max(mag[pos-w:pos+w])
        if local_peak/peak > thresh:
            ex.append(tone)

    return ex


def find_tones(fname):
    spacing = 0.7  # divide signal into chunks of this length
    rate, data, length = load_wav(fname)

    blocks = round(length/spacing)
    n = data.shape[0]
    w = n // blocks

    extracts = [0]*blocks
    for j in range(blocks):
        m = (j+1)*w
        if m > n:
            m = n
        block = data[j*w:(j+1)*w]
        freqs = np.array(range(0, block.shape[0]))/spacing
        df = fft(block)

        extracts[j] = extract_tone(freqs, df)

    pairs = tone_data()[2]
    ans = [pairs[(ex[0], ex[1])] for ex in extracts]
    return extracts, ans

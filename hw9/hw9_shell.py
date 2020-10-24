""" Code shell for HW 9, FFT problem.
Given:  tone_data (defines frequencies for digits),
        load_wav (loads a wav file)
        plus a few code stubs
"""

from numpy.fft import fft
from scipy.io import wavfile


def tone_data():
    """ Builds the data for the phone number sounds...
        Returns:
            tones - list of the freqs. present in the phone number sounds
            nums - a dictionary mapping the num. k to its two freqs.
            pairs - a dictionary mapping the two freqs. to the nums

        Each number is represented by a pair of frequencies: a 'low' and 'high'
        For example, 4 is represented by 697 (low), 1336 (high),
        so nums[4] = (697, 1336)
        and pairs[(697, 1336)] = 4
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

    tones = lows + highs  # combine to get total list of freqs.
    return tones, nums, pairs


def load_wav(fname):
    """ Loads a .wav file, returning the sound data.
        If stereo, converts to mono by averaging the two channels

        Returns:
            rate - the sample rate (in samples/sec)
            data - an np.array (1d) of the samples.
            length - the duration of the sound (sec)
    """
    rate, data = wavfile.read(fname)
    if len(data.shape) > 1 and data.shape[1] > 1:
        data = data[:, 0] + data[:, 1]  # stereo -> mono
    length = data.shape[0] / rate
    print(f"Loaded sound file {fname}.")
    return rate, data, length


# ----------------------------------------------------------------------
# example function stub for the homework

def identify_digit(fname):
    rate, data, length = load_wav(fname)

    # take fft of "data"...
    transform = fft(data)
    freq = ...

    # analyze transform to find digit
    ...

    if digit_is_found: # some kind of success condition...
        return digit
    else:
        ...  # (also account for digit not found)


def identify_dial(fname):
    tone_length = 0.7  # signal broken into 0.7 sec chunks with one num each
    rate, data, sound_length = load_wav(fname)

    # for each chunk, identify the digit
    ...

    # then print the number dialed at the end
    # (indicate which digits failed, if any, e.g. 555-24x1)
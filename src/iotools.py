"""This file contains reading and writing operations for audio files in 
wav format. A class called audio data with number of channels and samplerate 
associated with it. At a later point implementing it in terms of frames might 
be worth it, for easier translation to C/C++"""

import numpy as np
import sys
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile


class AudioData:
    """Object holding audio data and its associated samplerate and number of 
    channels
    """
    def __init__(self):
        self.filename = filename
        self.samplerate = samplerate
        self.number_of_channels = number_of_channels
        self.datatype = datatype
    pass

    def readfile(self, filename):
        """Reads a wav file into the AudioData object

        Args:
            filename (filename): full path to the wav file

        Returns:
            AudioData: Object containing the data, samplerate
            and number of channels

        TODO:

        """
        samplerate, data  = wavfile.read(filename)
        return samplerate, data

    def writefile(self):
        pass

    def append_data(self):
        pass

    def append_channel(self):
        pass

    def resample_data(self):
        pass

    def fill_data(self):
        pass

    def clear_data(self):
        pass
    
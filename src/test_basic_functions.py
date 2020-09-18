"""This script tests basic read/write functionality"""


import numpy as np
import sys
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

print(sys.path)


# write sinusoid to 16-bit, 44100 Hz PCM Mono 
samplerate = 187321 # samples/s
sinusoid_frequency = 1000 # Hz
length_seconds = 1.0 # seconds


t = np.linspace(0., length_seconds, int(np.rint(length_seconds*samplerate)))
# amplitude = np.iinfo(np.int32).max
amplitude = 1.0
data = amplitude*np.sin(2.*np.pi*sinusoid_frequency*t)
data = data.astype(np.float32)
wavfile.write("..//audio_examples//example_write.wav",samplerate, data )



samplerate2, data2 = wavfile.read("..//audio_examples//OneCD.wav")
nsamples = data2.shape[0]
t2 = np.linspace(0., nsamples/samplerate2, nsamples)
# plt.plot(t,data)
plt.plot(t2,data2[:,0])
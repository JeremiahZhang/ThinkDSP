from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display
from IPython.display import Audio

# Instantiate cosine and sine signals
cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

# Plot the signals. By default, plot plots three periods.
cos_sig.plot()
thinkplot.config(xlabel='Time(s)')
thinkplot.show()

sin_sig.plot()
thinkplot.config(xlabel='Time(s)')
thinkplot.show()

mix = sin_sig + cos_sig
mix.plot()
thinkplot.config(xlabel='Time(s)')
thinkplot.show()

# waves
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave.plot()
thinkplot.show()

audio = Audio(data=wave.ys, rate=wave.framerate)
audio.play()

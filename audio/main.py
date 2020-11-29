import wave
import numpy as np
import matplotlib.pyplot as plt
import pylab

with wave.open('audio.wav') as f:
	data = f.readframes(21)
	half = []
	for i in range(len(data)):
		if i % 6 == 2:
			half.append(data[i])

offset = len(half)%4
half = half[:-offset]
size = int(len(half)/4)

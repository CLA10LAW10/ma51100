import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Parameters
fs = 1000  # Sampling frequency in Hz
t = np.linspace(0, 0.5, int(fs * 0.5), endpoint=False)  # Time vector for 0.5 seconds
f1, f2 = 50, 150  # Frequencies
A1, A2 = 1, 0.5  # Amplitudes

# Individual signals
signal_50Hz = A1 * np.sin(2 * np.pi * f1 * t)
signal_150Hz = A2 * np.sin(2 * np.pi * f2 * t)

# Combined signal
signal_combined = signal_50Hz + signal_150Hz

# Compute the FFT
N = len(signal_combined)
yf = fft(signal_combined)
xf = fftfreq(N, 1 / fs)

# Plot all in one figure
plt.figure(figsize=(12, 12))

# 50 Hz Signal
plt.subplot(4, 1, 1)
plt.plot(t, signal_50Hz, label='50 Hz Signal', color='blue')
plt.title("50 Hz Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# 150 Hz Signal
plt.subplot(4, 1, 2)
plt.plot(t, signal_150Hz, label='150 Hz Signal', color='green')
plt.title("150 Hz Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Combined Signal
plt.subplot(4, 1, 3)
plt.plot(t, signal_combined, label='Combined Signal', color='red')
plt.title("Combined Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# FFT Plot
plt.subplot(4, 1, 4)
plt.plot(xf[:N//2], np.abs(yf[:N//2]), label='FFT Magnitude')
plt.title("Frequency-Domain Representation (FFT)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('project_fft.png')
plt.show()

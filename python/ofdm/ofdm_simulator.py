import numpy as np
import matplotlib.pyplot as plt

# Number of subcarriers
N = 8

# Generate random QPSK symbols
symbols = np.random.choice(
    [1+1j, -1+1j, -1-1j, 1-1j],
    N
)

print("QPSK Symbols:")
print(symbols)

# OFDM Modulation using IFFT
ofdm_signal = np.fft.ifft(symbols)

print("\nOFDM Signal:")
print(ofdm_signal)

# Plot real part
plt.figure(figsize=(10,4))

plt.plot(ofdm_signal.real)

plt.title("OFDM Signal (Real Part)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude")

plt.grid(True)

plt.savefig("results/ofdm_signal.png", dpi=300)

plt.show()
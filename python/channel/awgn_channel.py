import numpy as np
import matplotlib.pyplot as plt
samples = 1000

t = np.linspace(0, 1, samples)

signal = np.cos(2 * np.pi * 5 * t)

noise = np.random.normal(0, 0.3, samples)

received_signal = signal + noise

plt.figure(figsize=(12,5))

plt.plot(signal, label="Original Signal")

plt.plot(received_signal,
         label="Received Signal",
         alpha=0.7)

plt.title("AWGN Channel")

plt.xlabel("Sample Number")

plt.ylabel("Amplitude")

plt.legend()

plt.grid(True)

plt.savefig("results/awgn_channel.png", dpi=300)

plt.show()
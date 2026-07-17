import numpy as np
import matplotlib.pyplot as plt

snr_db = np.arange(0, 11, 1)

# Example BER values
ber = [0.18, 0.12, 0.08, 0.05, 0.03,
       0.015, 0.008, 0.004, 0.002,
       0.001, 0.0001]

plt.figure(figsize=(8,5))

plt.semilogy(snr_db, ber, marker='o')

plt.title("BER vs SNR for BPSK")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.grid(True)

plt.savefig("results/ber_vs_snr.png", dpi=300)

plt.show()
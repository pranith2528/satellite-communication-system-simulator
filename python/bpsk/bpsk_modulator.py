import numpy as np
import matplotlib.pyplot as plt
num_bits = 10
bits = np.random.randint(0, 2, num_bits)
print("Generated Bits:")
print(bits)
bpsk_symbols = np.where(bits == 1, 1, -1)
print("\nBPSK Symbols:")
print(bpsk_symbols)
plt.figure(figsize=(10,4))

plt.stem(range(num_bits), bpsk_symbols)

plt.title("BPSK Symbol Mapping")
plt.xlabel("Bit Index")
plt.ylabel("Symbol Value")
plt.grid(True)

plt.savefig("results/bpsk_symbol_mapping.png", dpi=300)

plt.show()
samples_per_bit = 100
carrier_frequency = 2

bpsk_wave = []

for symbol in bpsk_symbols:

    t = np.linspace(0, 1, samples_per_bit)

    carrier = np.cos(2 * np.pi * carrier_frequency * t)

    waveform = symbol * carrier

    bpsk_wave.extend(waveform)
plt.figure(figsize=(12,4))

plt.plot(bpsk_wave)
for i in range(nums_bits + 1):
    plt.axvline(i * samples_per_bit, linestyle='--', linewidth=0.8)
plt.title("BPSK Transmitted Waveform")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude")

plt.grid(True)

plt.savefig("results/bpsk_waveform.png", dpi=300)

plt.show()
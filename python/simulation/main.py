import numpy as np

# Step 1: Generate Random Bits
num_bits = 10
bits = np.random.randint(0, 2, num_bits)

print("Transmitted Bits:")
print(bits)

# Step 2: BPSK Modulation
bpsk_symbols = np.where(bits == 1, 1, -1)

print("\nBPSK Symbols:")
print(bpsk_symbols)

# Step 3: Add AWGN Noise
noise = np.random.normal(0, 0.5, num_bits)
received_symbols = bpsk_symbols + noise

print("\nReceived Symbols:")
print(received_symbols)

# Step 4: Demodulation
recovered_bits = np.where(received_symbols >= 0, 1, 0)

print("\nRecovered Bits:")
print(recovered_bits)

# Step 5: BER Calculation
errors = np.sum(bits != recovered_bits)
ber = errors / num_bits

print(f"\nNumber of Errors: {errors}")
print(f"BER: {ber}")
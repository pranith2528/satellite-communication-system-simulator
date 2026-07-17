import numpy as np

# Original transmitted bits
transmitted_bits = np.array([1, 0, 1, 1, 0, 1, 0])

# Received bits
received_bits = np.array([1, 0, 1, 0, 0, 1, 1])

print("Transmitted Bits:")
print(transmitted_bits)

print("\nReceived Bits:")
print(received_bits)

# Count errors
errors = np.sum(transmitted_bits != received_bits)

# Calculate BER
ber = errors / len(transmitted_bits)

print(f"\nNumber of Errors: {errors}")
print(f"Bit Error Rate (BER): {ber}")
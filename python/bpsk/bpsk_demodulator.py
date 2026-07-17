import numpy as np

# Example received symbols
received_symbols = np.array([1, -1, 1, 1, -1, 1, -1])

print("Received Symbols:")
print(received_symbols)

# Demodulation
recovered_bits = np.where(received_symbols >= 0, 1, 0)

print("\nRecovered Bits:")
print(recovered_bits)
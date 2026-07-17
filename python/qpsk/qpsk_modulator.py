import numpy as np

bits = np.random.randint(0, 2, 10)

# Make sure number of bits is even
if len(bits) % 2 != 0:
    bits = np.append(bits, 0)

print("Bits:")
print(bits)

symbols = []

for i in range(0, len(bits), 2):

    pair = (bits[i], bits[i+1])

    if pair == (0, 0):
        symbols.append(1 + 1j)

    elif pair == (0, 1):
        symbols.append(-1 + 1j)

    elif pair == (1, 1):
        symbols.append(-1 - 1j)

    else:
        symbols.append(1 - 1j)

print("\nQPSK Symbols:")
print(symbols)
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))

for symbol in symbols:
    plt.scatter(symbol.real, symbol.imag)

plt.axhline(0)
plt.axvline(0)

plt.title("QPSK Constellation Diagram")
plt.xlabel("In-Phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)

plt.savefig("results/qpsk_constellation.png", dpi=300)

plt.show()
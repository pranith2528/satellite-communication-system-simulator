import numpy as np
import matplotlib.pyplot as plt
num_bits = 1000
bits = np.random.randint(0, 2, num_bits)
print("First 20 bits:")
print(bits[:20])
zeros = np.sum(bits == 0)
ones = np.sum(bits == 1)
print(f"\nNumber of zeros: {zeros}")
print(f"Number of ones : {ones}")
zero_percentage = (zeros / num_bits) * 100
one_percentage = (ones / num_bits) * 100
print(f"Percentage of zeros: {zero_percentage:.2f}%")
print(f"Percentage of ones : {one_percentage:.2f}%")
plt.figure(figsize=(5,4))
plt.bar(['0', '1'], [zeros, ones])
plt.title("Distribution of Random Bits")
plt.xlabel("Bit Value")
plt.ylabel("Count")
plt.grid(axis='y')

plt.savefig("results/random_bits_distribution.png", dpi=300)
plt.show()
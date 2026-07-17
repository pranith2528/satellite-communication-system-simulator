import numpy as np
import matplotlib.pyplot as plt

num_samples = 1000

# Generate Rayleigh fading coefficients
rayleigh = np.random.rayleigh(scale=1, size=num_samples)

print("First 10 Rayleigh Coefficients:")
print(rayleigh[:10])

plt.figure(figsize=(10,4))

plt.plot(rayleigh)

plt.title("Rayleigh Fading Channel")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude")

plt.grid(True)

plt.savefig("results/rayleigh_channel.png", dpi=300)

plt.show()
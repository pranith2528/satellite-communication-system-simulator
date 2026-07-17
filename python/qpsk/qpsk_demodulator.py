symbols = [
    1+1j,
    -1+1j,
    -1-1j,
    1-1j
]

recovered_bits = []

for symbol in symbols:

    if symbol == (1+1j):
        recovered_bits.extend([0, 0])

    elif symbol == (-1+1j):
        recovered_bits.extend([0, 1])

    elif symbol == (-1-1j):
        recovered_bits.extend([1, 1])

    elif symbol == (1-1j):
        recovered_bits.extend([1, 0])

print("Recovered Bits:")
print(recovered_bits)
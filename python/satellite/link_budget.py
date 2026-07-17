import math

# Parameters
transmit_power_db = 30      # dBW
antenna_gain_tx = 40        # dB
antenna_gain_rx = 35        # dB
path_loss = 200             # dB

# Received Power
received_power = (
    transmit_power_db
    + antenna_gain_tx
    + antenna_gain_rx
    - path_loss
)

print("Satellite Link Budget")
print("----------------------")
print(f"Transmit Power : {transmit_power_db} dBW")
print(f"TX Gain        : {antenna_gain_tx} dB")
print(f"RX Gain        : {antenna_gain_rx} dB")
print(f"Path Loss      : {path_loss} dB")
print(f"\nReceived Power : {received_power} dBW")
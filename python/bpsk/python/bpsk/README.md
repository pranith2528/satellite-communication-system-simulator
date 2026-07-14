# BPSK Modulator

## Overview

This module implements a Binary Phase Shift Keying (BPSK) transmitter using Python.

The objective is to understand how digital binary data is converted into a phase-modulated carrier signal for transmission through a communication channel.

---

## Theory

Binary Phase Shift Keying (BPSK) is one of the simplest digital modulation techniques.

Each binary bit is represented by one of two possible phases of a carrier signal.

- Bit **1** → +1 (0° phase)
- Bit **0** → -1 (180° phase)

Mathematically,

s(t) = m × cos(2πfct)

where:

- m = +1 for bit 1
- m = -1 for bit 0
- fc = carrier frequency

---

## Project Workflow

Random Bit Generator

↓

BPSK Symbol Mapping

↓

Carrier Wave Generation

↓

Transmitted BPSK Signal

---

## Files

### bpsk_modulator.py

Implements:

- Random bit generation
- BPSK symbol mapping
- Carrier waveform generation
- Signal visualization

---

## Required Libraries

Install the required libraries using:

```bash
pip install numpy matplotlib
```

---

## How to Run

Open the project folder and execute:

```bash
py python/bpsk/bpsk_modulator.py
```

---

## Expected Output

The program displays:

- Generated random bits
- BPSK symbol sequence
- BPSK symbol mapping plot
- BPSK transmitted waveform

The figures are automatically saved inside the `results` folder.

---

## Learning Outcomes

After completing this module, you will understand:

- Binary data generation
- Digital modulation
- BPSK mapping
- Carrier signal generation
- Phase inversion
- Signal visualization using Matplotlib

---

## Future Improvements

This module will be extended with:

- AWGN Channel
- BPSK Demodulator
- BER Calculation
- BER vs SNR Analysis
- Rayleigh Fading Channel
- QPSK Modulation
- OFDM System
- Satellite Communication Link Budget

---

## Author

Pranith Reddy

Master's Preparation Project

Satellite Communication System Simulator
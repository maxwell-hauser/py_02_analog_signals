# Chapter 2: Analog Signals

## Overview

This chapter explores analog signals, their characteristics, and how they differ from digital signals. Analog signals are continuous-time signals that can take any value within a range.

## Key Concepts

### Analog Signal Fundamentals
- **Continuous Nature:** Analog signals vary smoothly over time
- **Infinite Values:** Can take any value within a range (unlike digital's discrete values)
- **Physical World:** Most natural phenomena produce analog signals (sound, light, temperature)

### Signal Characteristics

#### 1. Amplitude
- **Definition:** The maximum displacement from the equilibrium position
- **Measurement:** Typically measured in volts, decibels, or other units
- **Significance:** Determines signal strength or intensity

#### 2. Frequency
- **Definition:** Number of complete cycles per second
- **Unit:** Hertz (Hz), where 1 Hz = 1 cycle/second
- **Formula:** f = 1/T (frequency is inverse of period)
- **Common Ranges:**
  - Audio: 20 Hz - 20 kHz
  - Radio: kHz - GHz
  - Light: ~400-790 THz

#### 3. Period
- **Definition:** Time taken for one complete cycle
- **Unit:** Seconds (or milliseconds, microseconds)
- **Formula:** T = 1/f (period is inverse of frequency)

#### 4. Phase
- **Definition:** Position of a waveform relative to a reference point
- **Measurement:** Degrees (0°-360°) or radians (0-2π)
- **Phase Shift:** Difference in phase between two signals

### Waveforms

#### Sine Wave (Sinusoidal)
- **Formula:** y(t) = A × sin(2πft + φ)
  - A = amplitude
  - f = frequency
  - t = time
  - φ = phase shift
- **Properties:** Smooth, periodic, fundamental waveform in nature

#### Other Common Waveforms
- **Square Wave:** Alternates between two levels
- **Triangle Wave:** Linear rise and fall
- **Sawtooth Wave:** Linear rise, sharp drop (or vice versa)

## Learning Objectives

By the end of this chapter, you should be able to:
- Define analog signals and their characteristics
- Calculate frequency, period, and wavelength
- Understand the relationship between frequency and period
- Analyze amplitude and phase of signals
- Work with sine waves and their properties
- Distinguish between analog and digital representations

## Python Example

Run the interactive example:

```bash
python ch02_analog_signals.py
```

### What the Example Demonstrates

1. **Frequency and Period Calculations:** Computing f = 1/T and T = 1/f
2. **Sine Wave Generation:** Creating sinusoidal signals mathematically
3. **Amplitude Effects:** How amplitude affects signal strength
4. **Phase Shift:** Demonstrating phase differences between signals
5. **Signal Sampling:** Taking discrete samples of continuous signals
6. **Common Frequencies:** Examples from audio, radio, and other domains

### Sample Output

```
============================================================
CHAPTER 2: Analog Signals
============================================================

--- Example 1: Frequency and Period Relationship ---
For a signal with frequency 1000 Hz:
  Period T = 1/f = 1/1000 = 0.001 seconds (1.0 ms)

For a signal with period 0.002 seconds:
  Frequency f = 1/T = 1/0.002 = 500 Hz
...
```

## Real-World Applications

### Audio Systems
- **Microphones:** Convert sound (analog) to electrical signals
- **Speakers:** Convert electrical signals to sound waves
- **Music:** Pure tones are sine waves at specific frequencies
- **Voice:** Complex combination of multiple frequencies

### Radio Communications
- **AM Radio:** Amplitude Modulation (varies amplitude)
- **FM Radio:** Frequency Modulation (varies frequency)
- **Broadcasting:** Carrier waves at specific frequencies

### Sensors
- **Temperature:** Thermocouples produce analog voltage
- **Light:** Photodiodes generate current proportional to light intensity
- **Pressure:** Strain gauges output analog voltage

### Medical Equipment
- **ECG/EKG:** Heart electrical activity (analog waveform)
- **EEG:** Brain wave patterns
- **Ultrasound:** High-frequency sound waves

## Analog vs Digital

| Aspect | Analog | Digital |
|--------|--------|---------|
| **Values** | Continuous (infinite) | Discrete (finite) |
| **Representation** | Smooth curves | Step-like levels |
| **Noise Susceptibility** | High (accumulates) | Low (can be corrected) |
| **Storage** | Difficult (degrades) | Easy (exact copies) |
| **Processing** | Limited | Extensive (computers) |
| **Real World** | Natural signals | Computer systems |

## Common Questions

**Q: Why do we convert analog signals to digital?**  
A: Digital signals are easier to store, process, transmit, and reproduce without degradation. Computers can only work with discrete values.

**Q: What is sampling?**  
A: Sampling is the process of converting analog signals to digital by taking measurements at regular intervals.

**Q: What's the Nyquist theorem?**  
A: To accurately represent an analog signal digitally, you must sample at least twice the highest frequency present in the signal.

**Q: Can we perfectly reproduce analog signals from digital?**  
A: With sufficient sampling rate and bit depth, we can get very close, but there's always some information loss in the analog-to-digital conversion.

## Mathematical Relationships

### Basic Formulas
```
Frequency:        f = 1/T (Hz)
Period:           T = 1/f (seconds)
Angular Frequency: ω = 2πf (rad/s)
Wavelength:       λ = v/f (meters, where v = wave speed)

Sine Wave:        y(t) = A·sin(2πft + φ)
  where: A = amplitude
         f = frequency
         t = time
         φ = phase (radians)
```

## Key Takeaways

- Analog signals are continuous and can take infinite values within a range
- Frequency and period are inversely related: f = 1/T
- Amplitude, frequency, and phase are the three main characteristics
- 🎵 Natural phenomena (sound, light, temperature) are inherently analog
- Digital systems require converting analog signals through sampling
- Sine waves are the fundamental building blocks of complex signals

## Practice Exercises

1. Calculate the period of a 440 Hz signal (musical note A)
2. What is the frequency of a signal with a period of 50 microseconds?
3. Draw a sine wave and label its amplitude, period, and frequency
4. If a signal has frequency 1 kHz and is phase-shifted by 90°, write its equation
5. Explain why analog audio recordings degrade over time but digital recordings don't

## Further Study

- Explore digital signals in Chapter 3
- Learn about analog-to-digital conversion
- Study Fourier analysis (any signal can be decomposed into sine waves)
- Investigate sampling theory and the Nyquist-Shannon theorem

---

**Course Navigation:**  
← Previous: [Chapter 1 - Signals and Number Systems](../ch1_signal_and_num_sys/) | Next: [Chapter 3 - Digital Signals](../ch3_digital_signals/) →

---
<!-- License moved to dedicated LICENSE file -->

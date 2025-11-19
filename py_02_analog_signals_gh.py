#!/usr/bin/env python3
"""
Chapter 2: Analog Signals
Demonstrates analog signal properties: amplitude, frequency, phase, period
"""

import math

def calculate_frequency(period):
    """Calculate frequency from period: f = 1/T"""
    return 1.0 / period

def calculate_period(frequency):
    """Calculate period from frequency: T = 1/f"""
    return 1.0 / frequency

def sine_wave_value(amplitude, frequency, time, phase=0):
    """Calculate sine wave value at given time
    V(t) = A * sin(2πft + φ)
    """
    return amplitude * math.sin(2 * math.pi * frequency * time + phase)

def display_sine_wave_samples(amplitude=5, frequency=1, samples=20, phase=0):
    """Display sampled values of a sine wave"""
    print(f"\nSine Wave: Amplitude={amplitude}V, Frequency={frequency}Hz, Phase={phase}rad")
    print("Time(s) | Voltage(V)")
    print("-" * 30)
    
    duration = 2.0  # Show 2 complete cycles
    time_step = duration / samples
    
    for i in range(samples):
        t = i * time_step
        v = sine_wave_value(amplitude, frequency, t, phase)
        print(f" {t:.3f}  |  {v:+6.2f}")

def main():
    print("=" * 60)
    print("CHAPTER 2: Analog Signals")
    print("=" * 60)
    
    # Example 1: Frequency and Period relationship
    print("\n--- Example 1: Frequency and Period ---")
    period = 0.02  # 20 milliseconds
    frequency = calculate_frequency(period)
    print(f"Period (T):    {period} seconds")
    print(f"Frequency (f): {frequency} Hz")
    print(f"Relationship:  f = 1/T")
    
    # Example 2: Period from Frequency
    print("\n--- Example 2: Calculate Period ---")
    freq = 60  # 60 Hz (like AC power)
    period = calculate_period(freq)
    print(f"Frequency: {freq} Hz")
    print(f"Period:    {period:.6f} seconds")
    print(f"           {period * 1000:.3f} milliseconds")
    
    # Example 3: Sine Wave Characteristics
    print("\n--- Example 3: Analog Sine Wave Samples ---")
    display_sine_wave_samples(amplitude=5, frequency=1, samples=16)
    
    # Example 4: Phase Shift
    print("\n--- Example 4: Effect of Phase Shift ---")
    print("\nOriginal wave (phase = 0):")
    t = 0.25  # Quarter period
    v1 = sine_wave_value(5, 1, t, 0)
    print(f"At t=0.25s: V = {v1:.2f}V")
    
    print("\nPhase-shifted wave (phase = π/2):")
    v2 = sine_wave_value(5, 1, t, math.pi/2)
    print(f"At t=0.25s: V = {v2:.2f}V")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Analog signals are continuous")
    print("- Amplitude: maximum value of the signal")
    print("- Frequency: cycles per second (Hz)")
    print("- Period: time for one complete cycle")
    print("- Phase: horizontal shift of the waveform")
    print("=" * 60)

if __name__ == "__main__":
    main()

# ELE302 | Electric Networks

ELE302 extends circuit analysis to coupled inductors, transformers, three-phase systems, op-amps, transforms, frequency response, and two-port networks. Phasors turn a single-frequency sinusoidal problem into complex-number arithmetic while retaining amplitude and phase. [TMU course description](https://www.torontomu.ca/calendar/2026-2027/courses/electrical-engineering/ELE/302/).

## Worked example: current and power in an RL circuit

A 10 V RMS source drives a series resistor and ideal inductor at 1 kHz. Let the resistance be 30 Ω and the inductive reactance be 40 Ω. The required inductance is `L = 40 / (2π × 1000) ≈ 6.37 mH`.

Using the source voltage as the zero-phase reference:

```text
Z = 30 + j40 Ω = 50∠53.13° Ω
I = 10∠0° V / Z = 0.2∠−53.13° A RMS
```

Current lags voltage by 53.13°. The impedance magnitude determines current amplitude; its angle determines the time relationship.

Because the phasors use RMS values, complex power is `S = V × conjugate(I)`:

```text
P = |I|²R = 1.2 W
Q = |I|²XL = 1.6 var
|S| = 10 V × 0.2 A = 2 VA
Power factor = P / |S| = 0.6, lagging
```

The resistor dissipates real power. The ideal inductor exchanges energy with the source and contributes positive reactive power.

## Limit

This result applies after transients decay at the stated frequency. Immediately after switching, stored energy creates an additional transient that this phasor calculation omits.

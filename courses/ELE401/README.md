# ELE401 | Electric and Magnetic Fields

ELE401 connects charges, currents, fields, material properties, and geometry. Topics include electric potential, capacitance, magnetic forces, inductance, boundary conditions, and time-varying fields. A capacitor provides a direct example of geometry determining a circuit parameter. [TMU course description](https://www.torontomu.ca/calendar/2026-2027/courses/electrical-engineering/ELE/401/).

## Worked example: a parallel-plate capacitor

Consider two conducting plates with an overlapping area of 20 cm² and a separation of 0.5 mm. A uniform dielectric with relative permittivity 3 fills the gap. Connect the plates to a 12 V source.

Convert to SI units:

```text
A = 0.002 m²
d = 0.0005 m
ε = 3 × 8.854 × 10⁻¹² F/m
C = εA/d ≈ 106.25 pF
```

For the uniform-field model, the field magnitude is `E = V/d = 24,000 V/m`. Its direction is from the positive plate toward the negative plate. The charge magnitude on each plate is `Q = CV ≈ 1.275 nC`.

The stored energy is:

```text
W = ½CV² ≈ 7.65 nJ
```

If the separation doubles while the source maintains 12 V, capacitance, charge, field magnitude, and stored energy each fall by half. Keeping voltage fixed matters; disconnecting the source and holding charge fixed gives different changes.

## Limit

The formula neglects fields spreading around the plate edges. It becomes less accurate when the separation approaches the plates' lateral dimensions, because the field is no longer approximately uniform.

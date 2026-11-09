# Circuit calculations

Two small examples connect circuit equations with input validation and automated checks. They use the Python standard library and calculate ideal models.

## Loaded resistor divider

The source drives a series resistor. A shunt resistor connects the output to ground, and an optional load connects in parallel with the shunt.

```text
Vin ---- Rseries ----+---- Vout
                    |
                 Rshunt || Rload
                    |
                   GND
```

For positive resistances, the output is:

```text
Vout = Vin / (1 + Rseries/Rshunt + Rseries/Rload)
```

Omit the final term for an unloaded output. With 5 V and two 10 kΩ resistors, the unloaded output is 2.5 V. Adding a 10 kΩ load reduces it to 1.6667 V. The calculation assumes a voltage source with zero source resistance and constant resistor values.

## Ideal RC low-pass filter

A series resistor drives a capacitor to ground, with output measured across the capacitor:

```text
time constant = R C
cutoff = 1 / (2 pi R C)
magnitude = 1 / sqrt(1 + (2 pi f R C)^2)
step response = Vin (1 - exp(-t / (R C)))
```

With 1 kΩ and 1 µF, the time constant is 1 ms and cutoff is 159.1549 Hz. A 5 V step reaches 3.1606 V after 1 ms.

These equations assume ideal components, no output load, and an initially uncharged capacitor. Source resistance, component tolerances, and loading change the response.

## Run and check

Use Python 3.11 or later. From the repository root:

```bash
python -m examples.circuits
python -m pip install pytest ruff
python -m pytest
ruff check examples tests
ruff format --check examples tests
```

Pytest and Ruff are development tools; the calculations have no third-party runtime dependencies. Tests cover numerical results, invalid physical inputs, and extreme values. The calculations have not been checked against hardware measurements.

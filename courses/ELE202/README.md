# ELE202 | Electric Circuit Analysis

ELE202 introduces circuit variables, resistive networks, circuit theorems, energy storage, first-order transients, and sinusoidal steady-state analysis. The divider below illustrates why an output voltage depends on the connected load. [TMU course description](https://www.torontomu.ca/calendar/2026-2027/courses/electrical-engineering/ELE/202/).

## Worked example: a loaded voltage divider

Connect a 2 kΩ resistor from a 12 V supply to an output node, then a 1 kΩ resistor from that node to ground. With no external load, both resistors carry the same current:

```text
I = 12 V / (2 kΩ + 1 kΩ) = 4 mA
Vout = I × 1 kΩ = 4 V
```

The upper resistor dissipates 32 mW and the lower resistor dissipates 16 mW. Their combined 48 mW equals the power supplied by the source.

Now connect a 1 kΩ load between the output and ground. It sits in parallel with the lower resistor:

```text
Rlower = 1 kΩ || 1 kΩ = 500 Ω
Vout = 12 V × 500 Ω / 2500 Ω = 2.4 V
```

The load lowers the output by 40%. This is why a resistor divider cannot maintain its unloaded voltage while supplying an arbitrary load.

## Limit

These calculations assume ideal resistors and a fixed 12 V source. Resistor tolerance changes the division ratio; source resistance adds to the upper leg and lowers the output further.

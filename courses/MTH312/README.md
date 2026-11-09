# MTH312 | Differential Equations and Vector Calculus

MTH312 covers differential equations, transforms, systems of equations, Fourier series, and vector calculus, including applications to electric circuits. A first-order RC example makes the connection between a physical conservation law, an initial condition, and a time-dependent solution. [TMU course description](https://www.torontomu.ca/calendar/2026-2027/courses/mathematics/MTH/312/).

## Worked example: charging a capacitor

At time zero, connect an initially uncharged 100 μF capacitor to a 5 V source through a 10 kΩ resistor. Kirchhoff's voltage law and `i = C dv/dt` give:

```text
RC dv/dt + v = 5 V
v(0) = 0
τ = RC = 1 s
```

A constant particular solution is 5 V. The homogeneous solution is `K e^(−t/τ)`. Applying the initial condition gives K = −5 V, hence:

```text
v(t) = 5[1 − e^(−t/1 s)] V, for t ≥ 0
v(1 s) ≈ 3.161 V
v(3 s) ≈ 4.751 V
```

The current starts at `5 V / 10 kΩ = 0.5 mA` and decays with the same time constant. At three seconds, it is about 24.9 μA.

Substituting the voltage and its derivative back into the differential equation gives 5 V, which checks the solution.

## Limit

The zero-voltage initial condition is essential. If the capacitor starts at 2 V, the solution becomes `5 − 3e^(−t/1 s)` volts. Reusing the uncharged formula would predict the wrong initial voltage and current.

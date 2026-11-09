# Engineering notes on divider loading and RC response

These notes derive the equations implemented in [examples/circuits.py](examples/circuits.py), connect them to the existing [test cases](tests/test_circuits.py), and identify what the ideal models omit. They are study examples, not submitted laboratory results. All quantities passed to the functions use SI units: volts, ohms, farads, hertz, and seconds.

## 1. A divider is a circuit with an output resistance

An unloaded divider has a series resistor `Rs` and a shunt resistor `Rp`. An attached load `RL` also connects from the output node to ground. Kirchhoff's current law at that node gives:

```text
(Vin - Vout) / Rs = Vout / Rp + Vout / RL
Vin / Rs = Vout × (1/Rs + 1/Rp + 1/RL)
Vout = Vin / (1 + Rs/Rp + Rs/RL)
```

`divider_output` uses this final form. When the load argument is absent, it omits `Rs/RL`; it does not substitute a zero-ohm resistor. A zero-ohm load would short the output, which is a different physical circuit. The function rejects that input because its interface accepts strictly positive finite resistance values.

For a synthetic 5 V source with `Rs = Rp = 10 kΩ`, the unloaded voltage is 2.5 V. Add `RL = 10 kΩ` and the two paths to ground form 5 kΩ in parallel. The output becomes `5 × 5/15 = 1.6667 V`. The source current is now 0.3333 mA; 0.1667 mA flows through each grounded resistor. The naive calculation `5 × 10/20` ignores the new current path and overstates the output by 0.8333 V.

The Thevenin equivalent explains the tradeoff without repeating the full node equation:

```text
Vth = Vin × Rp / (Rs + Rp)
Rth = Rs × Rp / (Rs + Rp)
Vloaded = Vth × RL / (Rth + RL)
relative loading error = 1 - Vloaded/Vth = Rth / (Rth + RL)
```

Here `Rth = 5 kΩ`. To keep loading error at or below 1%, solve `Rth/(Rth + RL) <= 0.01`, which gives `RL >= 99 × Rth = 495 kΩ`. A high-impedance input is therefore part of the divider's operating assumption. Reducing both divider resistors reduces output resistance but increases standing current. Adding a buffer changes that tradeoff but introduces another component and its own operating limits.

This is also why a resistor divider alone is a poor model of a supply that must hold voltage as its load changes. The code calculates one equilibrium for a specified load; it does not implement regulation. `test_divider_loading` checks both the numerical result and the direction of the loading effect. `test_divider_voltage_sign_and_open_load_limit` checks zero and negative input voltages and a very large finite load.

## 2. The same RC time constant controls frequency and time response

For a series resistor driving a capacitor to ground, capacitor impedance is `1/(jωC)`. Applying the divider relation to impedances yields:

```text
H(jω) = [1/(jωC)] / [R + 1/(jωC)] = 1/(1 + jωRC)
|H(jω)| = 1 / sqrt(1 + (ωRC)^2)
τ = RC
fc = 1/(2πRC)
```

At `ωRC = 1`, the magnitude is `1/√2 ≈ 0.707107`, or approximately -3.0103 dB. The cutoff is not the frequency at which the output becomes zero. At ten times cutoff, magnitude is `1/√101 ≈ 0.099504`, about -20.0432 dB. The `rc_magnitude` function returns a linear voltage ratio, so a caller must apply `20 log10(ratio)` to express it in decibels.

With `R = 1 kΩ` and `C = 1 µF`, `τ = 1 ms` and `fc = 159.1549 Hz`. The differential equation for an initially uncharged capacitor is:

```text
C × dVout/dt = (Vin - Vout)/R
Vout(t) = Vin × [1 - exp(-t/τ)]
```

A 5 V step reaches 3.1606 V after one time constant and 4.9663 V after five. The steady-state value is approached asymptotically. It is incorrect to treat one time constant as the time at which charging finishes.

`rc_cutoff`, `rc_magnitude`, and `rc_step` share `_time_constant`, which validates the components and their product. The existing frequency-response tests check DC gain, the cutoff point, and a higher frequency. The step-response tests check the initial condition, one time constant, a negative input step, and the long-time limit.

The equations assume no load on the capacitor. A resistor attached across it changes both DC gain and the effective resistance seen by the capacitor. Reusing the unloaded formula after adding a load is a model error even if the arithmetic is exact.

## 3. Numerical validity and physical validity are separate

`_positive` rejects zero, negative, and nonfinite component values. `_nonnegative` rejects negative or nonfinite time and frequency. These rules express the supported passive-component model. They also stop `NaN` from silently spreading into subsequent results.

Finite inputs can still produce a nonrepresentable product. For example, `1e308 × 10` overflows a double-precision time constant, while `1e-300 × 1e-300` underflows to zero. `test_rejects_unrepresentable_time_constant` exercises both cases. A successful input check on each number individually would miss that failure.

`rc_step` evaluates `-expm1(-t/τ)` rather than directly subtracting `exp(-t/τ)` from one. When `t/τ` is tiny, the exponential is very close to one and direct subtraction loses relative precision. `rc_magnitude` uses `hypot(1, ωRC)` for its denominator instead of explicitly squaring a potentially large term. These are implementation choices for floating-point calculations, not changes to the circuit equations.

Component tolerance remains outside those checks. With a 1% resistor and 10% capacitor, the extreme cutoff values are `fc_nominal/(1.01 × 1.10)` and `fc_nominal/(0.99 × 0.90)`, about 143.2538 Hz and 178.6251 Hz. Perfect agreement with the nominal equation cannot prove that a physical filter meets a tighter cutoff requirement.

## Verification map and next experiment

| Claim | Existing evidence or proposed check |
| --- | --- |
| Loading reduces the divider output | `test_divider_loading` and the KCL derivation above |
| Cutoff magnitude is 1/√2 | `test_rc_cutoff_and_frequency_response` |
| A 5 V step reaches 3.1606 V at 1 ms | `test_rc_step_at_zero_and_one_time_constant` |
| Invalid physical inputs fail explicitly | Parameterized resistance, component, voltage, frequency, and time tests |
| Nominal calculations describe hardware | Not established by these software tests |

A proposed bench experiment would measure the divider with several known loads, then sweep the RC filter around its predicted cutoff. Record the source impedance, instrument input impedance, component measurements, and probe arrangement. Compare the measured response against a model that includes those loads before attributing disagreement to software. No such bench result is claimed here.

[Back to the repository](README.md)

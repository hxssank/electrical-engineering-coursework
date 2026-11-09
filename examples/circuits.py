"""Ideal DC divider and first-order RC calculations, using SI units.

These are new study examples, not submitted coursework or hardware measurements.
"""

from __future__ import annotations

import math


def _positive(value: float, name: str) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and greater than zero")


def _nonnegative(value: float, name: str) -> None:
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and nonnegative")


def _finite_voltage(voltage: float) -> None:
    if not math.isfinite(voltage):
        raise ValueError("input_voltage must be finite")


def _time_constant(resistance: float, capacitance: float) -> float:
    _positive(resistance, "resistance")
    _positive(capacitance, "capacitance")
    time_constant = resistance * capacitance
    _positive(time_constant, "R*C at floating-point precision")
    return time_constant


def divider_output(
    input_voltage: float,
    series_resistance: float,
    shunt_resistance: float,
    load_resistance: float | None = None,
) -> float:
    """Return DC output voltage, with an optional load parallel to the shunt.

    Assumes ideal resistors and an ideal voltage source with zero source resistance.
    Resistances are in ohms. Omitting the load represents an open-circuit output.
    """
    _finite_voltage(input_voltage)
    _positive(series_resistance, "series_resistance")
    _positive(shunt_resistance, "shunt_resistance")
    denominator = 1.0 + series_resistance / shunt_resistance
    if load_resistance is not None:
        _positive(load_resistance, "load_resistance")
        denominator += series_resistance / load_resistance
    return input_voltage / denominator


def rc_cutoff(resistance: float, capacitance: float) -> float:
    """Return the ideal unloaded RC low-pass -3 dB cutoff in hertz."""
    time_constant = _time_constant(resistance, capacitance)
    cutoff = (1.0 / math.tau) / time_constant
    _positive(cutoff, "cutoff at floating-point precision")
    return cutoff


def rc_magnitude(resistance: float, capacitance: float, frequency: float) -> float:
    """Return |Vout/Vin| for an ideal unloaded RC low-pass at frequency in Hz."""
    time_constant = _time_constant(resistance, capacitance)
    _nonnegative(frequency, "frequency")
    angular_term = math.tau * (frequency * time_constant)
    return 1.0 / math.hypot(1.0, angular_term)


def rc_step(
    input_voltage: float, resistance: float, capacitance: float, time: float
) -> float:
    """Return capacitor voltage at time in seconds after a DC input step.

    Assumes an initially uncharged capacitor, ideal components, and no output load.
    """
    _finite_voltage(input_voltage)
    time_constant = _time_constant(resistance, capacitance)
    _nonnegative(time, "time")
    return input_voltage * -math.expm1(-time / time_constant)


def main() -> None:
    """Print calculated examples without reading or controlling hardware."""
    print("Ideal calculations; no hardware measurements")
    print(f"5 V, 10 kohm / 10 kohm divider: {divider_output(5, 10000, 10000):.4f} V")
    loaded = divider_output(5, 10000, 10000, 10000)
    print(f"Same divider with a 10 kohm load: {loaded:.4f} V")
    cutoff = rc_cutoff(1000, 1e-6)
    print(f"1 kohm, 1 uF RC cutoff: {cutoff:.4f} Hz")
    print(f"RC magnitude at cutoff: {rc_magnitude(1000, 1e-6, cutoff):.6f}")
    print(f"5 V step after 1 ms: {rc_step(5, 1000, 1e-6, 0.001):.4f} V")


if __name__ == "__main__":
    main()

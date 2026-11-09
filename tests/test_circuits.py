import math

import pytest

from examples.circuits import divider_output, rc_cutoff, rc_magnitude, rc_step


def test_divider_loading() -> None:
    unloaded = divider_output(5, 10000, 10000)
    loaded = divider_output(5, 10000, 10000, 10000)
    assert unloaded == pytest.approx(2.5)
    assert loaded == pytest.approx(1.6666666666666667)
    assert loaded < unloaded
    assert divider_output(12, 2000, 1000, 1000) == pytest.approx(2.4)


def test_divider_voltage_sign_and_open_load_limit() -> None:
    assert divider_output(0, 1000, 2000) == 0
    assert divider_output(-9, 1000, 2000) == pytest.approx(-6)
    assert divider_output(5, 10000, 10000, 1e15) == pytest.approx(2.5)


def test_rc_cutoff_and_frequency_response() -> None:
    assert rc_cutoff(1000, 1e-6) == pytest.approx(159.15494309189535)
    assert rc_magnitude(1000, 1e-6, 0) == 1
    assert rc_magnitude(1000, 1e-6, 159.15494309189535) == pytest.approx(
        0.7071067811865476
    )
    assert rc_magnitude(1000, 1e-6, 1000) == pytest.approx(0.15717672547758985)


def test_rc_step_at_zero_and_one_time_constant() -> None:
    assert rc_step(5, 1000, 1e-6, 0) == 0
    assert rc_step(5, 1000, 1e-6, 0.001) == pytest.approx(3.1606027941427883)
    assert rc_step(-5, 1000, 1e-6, 0.001) == pytest.approx(-3.1606027941427883)
    assert rc_step(5, 1000, 1e-6, 0.1) == pytest.approx(5)


@pytest.mark.parametrize("invalid", [0, -1, math.nan, math.inf, -math.inf])
@pytest.mark.parametrize("position", [1, 2, 3])
def test_divider_rejects_invalid_resistances(invalid: float, position: int) -> None:
    values = [5.0, 1000.0, 1000.0, 1000.0]
    values[position] = invalid
    with pytest.raises(ValueError):
        divider_output(*values)


@pytest.mark.parametrize("invalid", [0, -1, math.nan, math.inf, -math.inf])
@pytest.mark.parametrize("position", [0, 1])
def test_rc_rejects_invalid_components(invalid: float, position: int) -> None:
    values = [1000.0, 1e-6]
    values[position] = invalid
    with pytest.raises(ValueError):
        rc_cutoff(*values)
    with pytest.raises(ValueError):
        rc_magnitude(*values, 100)
    with pytest.raises(ValueError):
        rc_step(5, *values, 0.001)


@pytest.mark.parametrize("invalid", [-1, math.nan, math.inf, -math.inf])
def test_rc_rejects_invalid_frequency_and_time(invalid: float) -> None:
    with pytest.raises(ValueError):
        rc_magnitude(1000, 1e-6, invalid)
    with pytest.raises(ValueError):
        rc_step(5, 1000, 1e-6, invalid)


@pytest.mark.parametrize("invalid", [math.nan, math.inf, -math.inf])
def test_rejects_nonfinite_voltage(invalid: float) -> None:
    with pytest.raises(ValueError):
        divider_output(invalid, 1000, 1000)
    with pytest.raises(ValueError):
        rc_step(invalid, 1000, 1e-6, 0.001)


@pytest.mark.parametrize("resistance,capacitance", [(1e308, 10), (1e-300, 1e-300)])
def test_rejects_unrepresentable_time_constant(
    resistance: float, capacitance: float
) -> None:
    with pytest.raises(ValueError):
        rc_cutoff(resistance, capacitance)

# ELE404 | Electronic Circuits I

ELE404 covers diodes, transistor operating regions, biasing, small-signal amplifiers, current sources, and differential circuits. A linear model describes small changes around a device's DC operating point. [TMU course description](https://www.torontomu.ca/calendar/2026-2027/courses/electrical-engineering/ELE/404/).

## Worked example: common-emitter small-signal gain

Assume a forward-active BJT biased at a collector current of 1 mA. Use a thermal voltage of 25 mV and current gain β = 100. The emitter is grounded for AC signals. A 2 kΩ collector resistor and a 2 kΩ AC load both connect to AC ground.

Neglecting the transistor's output resistance:

```text
gm = IC / VT = 0.001 / 0.025 = 0.04 S
rπ = β / gm = 2.5 kΩ
Rload = 2 kΩ || 2 kΩ = 1 kΩ
Av = −gm × Rload = −40 V/V
```

An actual base-emitter signal of 2 mV peak therefore produces an estimated collector output of 80 mV peak, inverted. Its estimated collector-current variation is 80 μA peak.

Source resistance and the amplifier input resistance form a divider. A generator setting can therefore exceed the voltage reaching the base.

## Limit

The gain assumes a small base-emitter variation and forward-active operation. A 40 mV peak input is larger than the assumed thermal voltage. Extending the linear model that far predicts a 1.6 mA current swing around a 1 mA bias, so the small-signal approximation fails.

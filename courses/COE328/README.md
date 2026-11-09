# COE328 | Digital Systems

COE328 covers Boolean algebra, number representation, combinational and sequential logic, hardware description languages, and programmable logic devices. Arithmetic circuits connect a Boolean specification with a numerical result that can be checked for every input combination. [TMU course description](https://www.torontomu.ca/calendar/2026-2027/courses/computer-engineering/COE/328/).

## Worked example: a one-bit full adder

A full adder accepts bits A, B, and carry-in Cin. It produces a sum bit S and carry-out Cout. The required invariant is `A + B + Cin = S + 2 × Cout`.

|A|B|Cin|S|Cout|
|---|---|---|---|---|
|0|0|0|0|0|
|0|0|1|1|0|
|0|1|0|1|0|
|0|1|1|0|1|
|1|0|0|1|0|
|1|0|1|0|1|
|1|1|0|0|1|
|1|1|1|1|1|

The sum is `A XOR B XOR Cin`. Carry is `(A AND B) OR (A AND Cin) OR (B AND Cin)`: at least two input bits must be one.

For A = 1, B = 0, and Cin = 1, the input total is two, so S = 0 and Cout = 1. Connecting each carry-out to the next stage's carry-in gives a wider adder. Four stages compute `1011 + 0110 = 10001`, or 11 + 6 = 17.

## Limit

The truth table describes settled logic values. Carry propagation takes time, so sampling a multi-bit result before its longest carry path settles can capture an incorrect value.

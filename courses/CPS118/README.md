# CPS 118 | Introductory Programming for Scientists

Scientific programming turns a calculation into a repeatable procedure. The course covers arrays, program control, functions, numerical methods, and plotting, using MATLAB with an introduction to Python.

## Array calculation

An illustrative MATLAB calculation for three voltage samples is:

```matlab
voltage = [3.1, 3.2, 3.3];
averageVoltage = mean(voltage);
```

The mean is 3.2 V. A larger analysis should also state how missing values, sensor limits, and unequal sampling intervals are handled. An arithmetic mean treats each element equally; it is not automatically a time-weighted average.

Functions can separate data loading, calculation, and plotting. That separation makes it possible to check the numerical result with a small known input before applying the same procedure to an experimental dataset.

Course scope: [Toronto Metropolitan University, CPS 118](https://www.cs.torontomu.ca/~cps118/).

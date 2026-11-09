# COE 318: Software Systems

COE 318 connects object-oriented programming with requirements, implementation, testing, and debugging. It examines how classes and modules divide a program's responsibilities and how those parts work together. [TMU course outline](https://www.ee.torontomu.ca/undergraduate/outlines/COE318_course_outline.html)

## Study topics

- Java classes, constructors, instance state, static state, and interfaces.
- Object composition through accounts, card collections, and circuit components.
- Input validation and exceptions for invalid object state.
- Unit tests that check returned values and object relationships.

The retained course material includes complex-number arithmetic, bank accounts, a blackjack model, and circuit representations with nodes, resistors, and voltage sources. The circuit examples connect software design to electrical engineering: component objects store values and connections, while a circuit object collects the components.

## Study example

This example was written for this page.

A resistor model holds a resistance and two node identifiers. A circuit model holds a collection of components. Keeping those responsibilities separate lets a test check whether a resistor rejects a negative resistance without creating a whole circuit.

A useful test boundary is zero ohms. The requirements must decide whether the model accepts an ideal short circuit or requires strictly positive resistance. The constructor and its tests should implement the same decision.

## Engineering connection

The same separation applies to instrument drivers, simulation inputs, and embedded software. A component model records state; a separate calculation or controller uses that state. Recording a circuit's connectivity does not solve its voltages or currents.

This page contains original study notes, not submitted lab solutions.

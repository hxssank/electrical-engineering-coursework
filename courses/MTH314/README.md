# MTH314 | Discrete Mathematics for Engineers

MTH314 covers sets, relations, logic, sequences, mathematical reasoning, combinatorics, graphs, trees, and Boolean algebra. Graphs turn relationships into objects that can be counted and checked. A degree calculation can expose an inconsistent network description before an algorithm processes it. [TMU course description](https://www.torontomu.ca/calendar/2026-2027/courses/mathematics/MTH/314/).

## Worked example: checking an undirected graph

Let the vertices be A, B, C, and D, with edges AB, AC, BC, and CD. An edge joins two vertices; its order does not matter in this undirected graph.

|Vertex|Incident edges|Degree|
|---|---|---|
|A|AB, AC|2|
|B|AB, BC|2|
|C|AC, BC, CD|3|
|D|CD|1|

The degree sum is `2 + 2 + 3 + 1 = 8`. Each edge contributes one endpoint at each end, so it contributes two to the sum. Therefore `|E| = 8/2 = 4`, matching the listed edges.

This also explains why the number of odd-degree vertices must be even. An even total cannot contain an odd number of odd terms. Here C and D are the two odd-degree vertices.

## Limit

An even degree sum is necessary but does not prove that a proposed simple graph exists. On four vertices, the degree sequence `3, 3, 3, 1` sums to ten but is impossible: the three degree-three vertices must each connect to the remaining vertex, giving it degree three rather than one.

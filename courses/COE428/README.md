# COE 428: Engineering Algorithms and Data Structures

COE 428 covers algorithm design, time and space complexity, recursion, sorting, searching, and data structures. The curriculum also includes trees, hashing, and graph algorithms. [TMU course outline](https://www.ee.torontomu.ca/undergraduate/outlines/COE428_course_outline.html)

## Study topics

- Compare incremental algorithms with divide-and-conquer algorithms.
- Trace recursive calls and reason about their cost.
- Use arrays, pointers, stacks, and heaps in C.
- Count comparisons and copies to examine sorting behavior.
- Represent state transitions explicitly and validate input before using it as an index.

The retained lab material includes insertion sort, merge sort, a Towers of Hanoi recursion trace, an eight-state machine, and stack and heap exercises. These examples connect an algorithm's rules to memory layout and program behavior.

## Study example

This example was written for this page.

A max-heap stored as `[11, 7, 9, 2]` keeps each parent at least as large as its children. Inserting `12` first appends it, then swaps it upward past `7` and `11`. The result is `[12, 11, 9, 2, 7]`.

Reading the maximum takes constant time. Insertion and maximum removal take logarithmic time in the worst case because they follow a path through the heap. This suits a queue that repeatedly selects the highest-priority item.

## Engineering connection

Algorithm choice affects memory use and response time in embedded systems. Complexity bounds describe how work grows with input size; target-hardware measurements establish actual timing. A fixed-capacity C heap also needs an explicit full-capacity check before insertion to avoid an out-of-bounds write.

This page contains original study notes, not submitted lab solutions.

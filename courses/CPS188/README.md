# CPS 188 | Computer Programming Fundamentals

C programming provides direct control over data representation and memory access. Course topics include control flow, functions, arrays, pointers, structures, recursion, dynamic allocation, and input/output.

## Array bounds

For an array containing four elements, valid indices are 0 through 3. A loop that uses `i <= 4` accesses memory outside that array. The boundary should instead follow the array length:

```c
for (size_t i = 0; i < count; ++i) {
    /* Process element i. */
}
```

This fragment assumes `count` matches the number of accessible elements and that `size_t` is declared by the surrounding program. A pointer alone does not carry an array's length. Passing the length with the pointer makes that requirement explicit.

Course scope: [Toronto Metropolitan University, CPS 188](https://www.torontomu.ca/calendar/2026-2027/courses/computer-science/CPS/188/).

## Tower of Hanoi Recurrence Analysis

For the Tower of Hanoi problem where T(N) = 2·T(N-1) + 1 for N > 0 and T(0) = 0, what is the time complexity and what does this imply?

---

The recurrence T(N) = 2·T(N-1) + 1 is solved by substitution:
- T(N) = 2·T(N-1) + 1
- T(N) = 2²·T(N-2) + 2 + 1
- T(N) = 2³·T(N-3) + 2² + 2 + 1
- T(N) = 2^N·T(0) + (2^(N-1) + ... + 2 + 1)
- T(N) = 2^N - 1

Time complexity: O(2^N) - exponential time

Implication: For N=64 disks, this requires about 1.8×10^19 moves, taking ~585 billion years at one move per second.


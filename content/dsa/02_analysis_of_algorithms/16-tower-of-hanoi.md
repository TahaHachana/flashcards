## Tower of Hanoi Complexity

What is the recurrence relation and final time complexity for the Tower of Hanoi puzzle with N disks? Why is this significant?

---

**Recurrence Relation**:
T(N) = 0, if N = 0
T(N) = 2T(N-1) + 1, if N > 0

**Solution**: T(N) = 2ᴺ - 1

**Time Complexity**: O(2ᴺ) - Exponential!

**Significance**: For 64 disks (legendary puzzle), requires 2⁶⁴ - 1 ≈ 1.8 × 10¹⁹ moves. At 1 move/second, takes 585 billion years - demonstrating why exponential algorithms are impractical.


## Data Race Definition

What three conditions must all be true for a data race to occur?

---

A data race occurs when: (1) Two or more threads access the same memory location, (2) At least one access is a write, and (3) The accesses are not synchronized. All three conditions must be met simultaneously for it to be a data race.


## Data Race Definition

What is a data race, and what three conditions must all be met for one to occur?

---

A data race occurs when: (1) Two or more threads access the same memory location, (2) At least one access is a write, and (3) The accesses are not synchronized. All three conditions must be true simultaneously. Data races cause undefined behavior, making them catastrophic bugs that can lead to crashes, corruption, or security vulnerabilities.


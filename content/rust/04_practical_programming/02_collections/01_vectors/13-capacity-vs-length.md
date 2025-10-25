## Capacity vs Length

Define `.len()` and `.capacity()` for vectors. Why are they different?

---

- `.len()`: Current number of elements in the vector
- `.capacity()`: Total allocated space (can hold this many elements without reallocating)

They differ because vectors pre-allocate extra space to avoid frequent reallocations as you add elements.


## HashMap Length and Capacity

What's the difference between `.len()` and `.capacity()` for HashMap?

---

`.len()`: Number of key-value pairs currently stored

`.capacity()`: Total allocated space before needing to rehash

Like Vec, HashMap pre-allocates space and grows (rehashes) when capacity is exceeded. Use `HashMap::with_capacity(n)` to pre-allocate.


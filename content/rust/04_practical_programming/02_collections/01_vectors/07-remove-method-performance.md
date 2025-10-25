## Remove Method Performance

Why is `.remove(0)` slow on large vectors, and what's the alternative for efficient front removal?

---

`.remove(index)` shifts all elements after the index one position left, making it O(n). For frequent front removals, use `VecDeque` which has `O(1)` `pop_front()` using a ring buffer.


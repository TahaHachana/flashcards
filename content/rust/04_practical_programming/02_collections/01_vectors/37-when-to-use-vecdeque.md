## When to Use VecDeque

When should you use `VecDeque` instead of `Vec`? What's the tradeoff?

---

Use `VecDeque` when you need efficient operations on **both ends** (front and back). It has O(1) `push_front()` and `pop_front()` unlike Vec. Tradeoff: Slightly slower for other operations due to ring buffer implementation.


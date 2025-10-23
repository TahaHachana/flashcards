## Why Borrowing is Safe

What guarantees does the compiler enforce for borrowing?

---

No use-after-free (references can't outlive data), no data races (can't have simultaneous mutable access), and no dangling references (references always point to valid data). All at compile time with zero runtime cost.


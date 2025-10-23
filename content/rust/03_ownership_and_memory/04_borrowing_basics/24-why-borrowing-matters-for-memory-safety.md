## Why Borrowing Matters for Memory Safety

How does borrowing contribute to memory safety?

---

Compiler prevents use-after-free and dangling references by ensuring references can't outlive data. All checked at compile time with zero runtime cost.


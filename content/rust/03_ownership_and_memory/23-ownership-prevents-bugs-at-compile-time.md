## Ownership Prevents Bugs at Compile Time

When does the compiler enforce ownership rules?

---

At compile time. The compiler prevents using moved values, catching use-after-free and double-free bugs before the program runs. No runtime checks needed.


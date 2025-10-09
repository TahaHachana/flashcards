## Data Race Prevention

How does ownership prevent data races in concurrent programs?

---

Mutable access requires exclusive ownership. The compiler enforces that you cannot have multiple threads mutating shared data simultaneously, making data races impossible at compile time.


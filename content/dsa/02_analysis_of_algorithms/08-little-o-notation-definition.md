## Little o Notation Definition

Define little o notation o(g(n)) and how does it differ from Big O?

---

f(n) = o(g(n)) if f(n) = O(g(n)) AND f(n) ≠ Ω(g(n)). Mathematically: lim(n→∞)[f(n)/g(n)] = 0.

Little o represents a strict upper bound - f(n) grows strictly slower than g(n). Unlike Big O which allows functions to grow at the same rate, little o requires f(n) to grow slower than g(n).


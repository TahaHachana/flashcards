## Little o Notation

How does little o notation differ from Big O, and what does lim(n→∞) f(n)/g(n) = 0 tell us?

---

**Little o**: f(n) = o(g(n)) means f(n) = O(g(n)) but f(n) ≠ Ω(g(n))

The limit condition lim(n→∞) f(n)/g(n) = 0 means f(n) grows **strictly slower** than g(n).

**Key difference**: 
- Big O: f can grow at same rate as g (or slower)
- Little o: f must grow strictly slower than g

Example: 18n + 9 = o(n²) because linear grows strictly slower than quadratic, but 18n + 9 ≠ o(n).


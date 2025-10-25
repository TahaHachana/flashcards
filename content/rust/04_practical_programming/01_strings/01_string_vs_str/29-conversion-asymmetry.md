## Conversion Asymmetry

Why is conversion asymmetric between String and &str?

---

String → &str is cheap (borrow): just creates a reference, no allocation.
&str → String is expensive (allocate): must allocate heap memory and copy data.

This asymmetry reflects the underlying operations: borrowing is free, but creating owned copies requires resources. Rust makes the expensive direction explicit to prevent accidental performance issues.


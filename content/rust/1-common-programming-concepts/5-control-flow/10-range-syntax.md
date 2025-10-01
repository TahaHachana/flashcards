## Range Syntax

What is the difference between `..` and `..=` in Rust ranges?

---

* `start..end` → range is **exclusive** of the upper bound.
* `start..=end` → range is **inclusive** of the upper bound.

```rust
for n in 1..4 { println!("{n}"); }   // 1, 2, 3
for n in 1..=4 { println!("{n}"); }  // 1, 2, 3, 4
```


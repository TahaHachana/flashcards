## Exclusive vs Inclusive Ranges

What's the difference between .. and ..= in ranges?

---

.. is exclusive (doesn't include end), ..= is inclusive (includes end).

```rust
1..5   // 1, 2, 3, 4 (excludes 5)
1..=5  // 1, 2, 3, 4, 5 (includes 5)
```


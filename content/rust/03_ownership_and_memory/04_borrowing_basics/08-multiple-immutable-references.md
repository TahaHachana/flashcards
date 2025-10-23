## Multiple Immutable References

Can you have multiple immutable references at the same time?

---

Yes. Multiple readers are safe since all references are read-only with no risk of conflicts.

```rust
let s = String::from("hello");
let r1 = &s;
let r2 = &s;
let r3 = &s;  // ✅ All valid
```


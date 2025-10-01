## Mixed References

Can mutable and immutable references coexist to the same value?

---

No. You cannot have a mutable reference and immutable references at the same time.
They must be separated by scope.

```rust
let mut s = String::from("hello");

let r1 = &s; // immutable
let r2 = &s; // immutable
// let r3 = &mut s; // ❌ not allowed here
```


# Automatic Referencing and Dereferencing

How does Rust handle receiver referencing/dereferencing when calling methods?

---

Rust automatically inserts &, &mut, or * to make the receiver match the method signature.

```rust
p1.distance(&p2); // same as (&p1).distance(&p2)
```
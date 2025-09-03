# Immutable References

How many immutable references to the same data are allowed in a given scope?

---

You can have any number of immutable references (`&T`) simultaneously. They only permit read-only access.

```rust
let s = String::from("hello");
let r1 = &s;
let r2 = &s;
println!("{} and {}", r1, r2);
```
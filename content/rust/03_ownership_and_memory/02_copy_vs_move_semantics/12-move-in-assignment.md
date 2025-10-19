## Move in Assignment

What happens when you assign a non-Copy type to a new variable?

---

Ownership moves. The original variable becomes invalid.

```rust
let s1 = String::from("hello");
let s2 = s1;
println!("{}", s1);  // ❌ Error: s1 moved
```


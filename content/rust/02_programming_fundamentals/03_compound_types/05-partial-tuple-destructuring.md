## Partial Tuple Destructuring

How do you ignore specific values when destructuring a tuple?

---

Use underscore (_) for values you don't need.

```rust
let tup = (500, 6.4, 1);
let (x, _, z) = tup;  // Ignore middle value
println!("{}, {}", x, z);  // 500, 1
```


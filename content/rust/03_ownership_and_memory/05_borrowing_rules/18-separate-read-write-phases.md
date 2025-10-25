## Separate Read Write Phases

What's the correct pattern for mixing immutable and mutable borrows?

---

Clear separation: read phase with immutable references first, then write phase with mutable reference after immutable refs are done.

```rust
let r1 = &s;
println!("{}", r1);  // Read phase ends
let r2 = &mut s;  // Write phase begins
```


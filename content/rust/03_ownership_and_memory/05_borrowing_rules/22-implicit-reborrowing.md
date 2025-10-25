## Implicit Reborrowing

When does implicit reborrowing occur?

---

When passing a mutable reference to a function expecting an immutable reference.

```rust
fn read(s: &String) { }
let r = &mut s;
read(r);  // Implicit reborrow as &String
r.push_str("!");  // r still valid
```


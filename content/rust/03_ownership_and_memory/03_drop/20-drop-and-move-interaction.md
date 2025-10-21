## Drop and Move Interaction

What happens to drop responsibility when a value is moved?

---

Drop responsibility transfers to the new owner. The original owner won't be dropped.

```rust
let r1 = Resource::new();
let r2 = r1;  // Ownership moves
// Only r2 is dropped, not r1
```


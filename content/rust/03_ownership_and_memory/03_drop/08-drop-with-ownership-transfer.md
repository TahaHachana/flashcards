## Drop with Ownership Transfer

What happens to drop when ownership is moved?

---

The new owner becomes responsible for dropping. The original owner is invalid and won't be dropped.

```rust
let s1 = String::from("hello");
let s2 = s1;  // Ownership moves
// Only s2 is dropped, not s1
```


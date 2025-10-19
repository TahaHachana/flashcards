## Multiple Ownership Transfers

What happens when ownership is transferred multiple times?

---

Ownership moves through the chain. Only the final owner is valid; all previous owners are invalidated.

```rust
let s1 = String::from("hello");
let s2 = s1;  // s1 invalid
let s3 = s2;  // s2 invalid
// Only s3 is valid
```


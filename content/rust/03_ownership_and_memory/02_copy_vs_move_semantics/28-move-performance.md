## Move Performance

Is moving always fast?

---

Yes. Moving large types like Vec is fast because it only copies the stack portion (pointer/len/cap), not the heap data.

```rust
let v1 = vec![0; 1_000_000];
let v2 = v1;  // Fast: just copies pointer
```


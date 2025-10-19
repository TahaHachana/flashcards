## Clone Performance

Is cloning always fast?

---

No. Clone can be slow because it allocates and copies all data, including heap contents.

```rust
let v1 = vec![0; 1_000_000];
let v2 = v1.clone();  // Slow: copies million elements
```


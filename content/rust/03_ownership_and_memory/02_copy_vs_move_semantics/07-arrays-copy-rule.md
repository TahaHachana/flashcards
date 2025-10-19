## Arrays Copy Rule

When is an array Copy?

---

Only if its element type is Copy.

```rust
let a: [i32; 3] = [1, 2, 3];              // Copy
let b: [String; 2] = [s1, s2];            // NOT Copy
```


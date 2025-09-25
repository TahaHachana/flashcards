## Expressions in Blocks

How can a block return a value in Rust?

---

A block without a semicolon on its final line is an expression whose value is returned.

Example:
```rust
let y = {
    let x = 3;
    x + 1 // returns 4
};
```


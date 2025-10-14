## Block Expressions

What value does a block expression evaluate to?

---

Blocks evaluate to their last expression (if it doesn't have a semicolon).

```rust
let x = {
    let price = 10;
    let quantity = 3;
    price * quantity  // Block evaluates to 30
};
```


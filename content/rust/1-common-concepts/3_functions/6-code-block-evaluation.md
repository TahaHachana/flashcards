# Code Block Evaluation

What does this code block evaluate to?
```rust
let y = {
    let x = 3;
    x + 1
};
```

---

`y` will be `4`. The block is an expression that evaluates to `x + 1` (which is `4`). Note there's no semicolon after `x + 1`, making it an expression that returns a value.
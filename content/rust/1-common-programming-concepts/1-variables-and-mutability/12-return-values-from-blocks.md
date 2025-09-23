## Return Values From Blocks

How can a block of code be used as the value of a variable?

---

The final expression in a block (without `;`) becomes its return value.

```rust
let y = {
    let x = 3;
    x + 1 // y = 4
};
```


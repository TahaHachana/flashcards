## Statements Don't Return Values

Can you assign a statement to a variable?

---

No. Statements don't have values, so you can't assign them.

```rust
let x = (let y = 6);  // ❌ Error: let is a statement
```


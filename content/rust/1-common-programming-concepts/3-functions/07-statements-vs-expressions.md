## Statements Vs Expressions

What is the difference between statements and expressions in Rust?

---

* **Statements**: Perform actions but don’t return values (e.g., `let y = 6;`).
* **Expressions**: Produce a value (e.g., `5 + 6`, function calls, blocks).
* Adding a semicolon to an expression makes it a statement.

```rust
let y = {
    let x = 3;
    x + 1 // expression
};
```


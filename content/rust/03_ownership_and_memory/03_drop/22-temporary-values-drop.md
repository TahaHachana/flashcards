## Temporary Values Drop

When are temporary values dropped?

---

At the end of the statement that creates them.

```rust
let len = String::from("temp").len();
// Temporary String dropped here
```


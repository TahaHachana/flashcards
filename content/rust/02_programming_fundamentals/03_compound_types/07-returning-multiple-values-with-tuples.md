## Returning Multiple Values with Tuples

How can functions return multiple values using tuples?

---

Return a tuple containing multiple values, then destructure it.

```rust
fn calculate(x: i32) -> (i32, i32) {
    (x * 2, x * 3)
}
let (doubled, tripled) = calculate(5);
```


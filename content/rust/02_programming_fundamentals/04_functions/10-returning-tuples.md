## Returning Tuples

How do you return multiple values from a function?

---

Return a tuple containing multiple values.

```rust
fn calculate(x: i32) -> (i32, i32, i32) {
    (x + 1, x * 2, x * x)
}
let (inc, dbl, sqr) = calculate(5);
```


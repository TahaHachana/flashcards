## Gotcha Multiple Returns Different Sources

Why might returning references with different lifetimes in a tuple be problematic?

```rust
fn problematic<'a, 'b>(x: &'a str, y: &'b str) -> (&'a str, &'b str) {
    (x, y)
}
```

---

While this compiles, it can be difficult for callers to work with because the two elements of the tuple have different lifetimes. Often it's better to require both to have the same lifetime:
```rust
fn fixed<'a>(x: &'a str, y: &'a str) -> (&'a str, &'a str)
```
This makes it clear to the caller how long the entire return value is valid—as long as both inputs are valid.


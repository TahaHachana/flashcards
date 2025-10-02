## Let Else Basics

What does `let else` do in Rust?

---

It matches a value against a pattern and exits early if the match fails:

```rust
fn parse(input: Option<i32>) -> i32 {
    let Some(x) = input else {
        return 0;
    };
    x * 2
}
```


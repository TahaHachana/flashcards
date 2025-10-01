## Loop Returning Value

How can a `loop` return a value in Rust?

---

A `break` statement can return a value, which becomes the loop’s result.

```rust
let result = loop {
    counter += 1;
    if counter == 10 {
        break counter * 2;
    }
};
```


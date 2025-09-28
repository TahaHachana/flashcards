## Doc Tests

What are Rust doc tests and how do you control their execution?

---

Code blocks in doc comments are compiled and tested by default with `cargo test`.
You can control them with attributes:

* `no_run` → compile but don’t run.
* `ignore` → skip compilation and execution.

```rust
/// ```no_run
/// println!("This compiles but doesn't run");
/// ```
```


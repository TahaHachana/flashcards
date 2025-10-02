## Option Enum Usage

What does the `Option<T>` enum represent?

---

`Option<T>` represents either:

* `Some(T)` — a present value.
* `None` — absence of a value.

```rust
let x: Option<i32> = Some(5);
let y: Option<i32> = None;
```


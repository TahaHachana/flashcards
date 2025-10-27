## Ok Or Method

How do you convert an `Option<T>` to a `Result<T, E>`?

---

Use `ok_or()` or `ok_or_else()`:

```rust
let some_value = Some(42);
let result: Result<i32, &str> = some_value.ok_or("No value");
// Ok(42)

let none_value: Option<i32> = None;
let result: Result<i32, &str> = none_value.ok_or("No value");
// Err("No value")
```

`ok_or()` transforms `Some(v)` → `Ok(v)` and `None` → `Err(e)`.


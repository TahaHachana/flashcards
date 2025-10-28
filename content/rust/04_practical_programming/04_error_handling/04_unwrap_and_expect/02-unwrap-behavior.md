## Unwrap Behavior

What exactly happens when you call `unwrap()` on a `Result` or `Option`?

---

`unwrap()` extracts the success value or panics with a generic message:

```rust
let result: Result<i32, &str> = Ok(42);
let value = result.unwrap();  // 42

let error: Result<i32, &str> = Err("failed");
let value = error.unwrap();  // PANIC: called `Result::unwrap()` on an `Err` value

let some = Some(10);
let value = some.unwrap();  // 10

let none: Option<i32> = None;
let value = none.unwrap();  // PANIC: called `Option::unwrap()` on a `None` value
```

When it panics: stack unwinds, destructors run, error printed to stderr, program terminates with non-zero exit code.


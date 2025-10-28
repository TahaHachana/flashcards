## Map Method On Result

What does the `map()` method do on a `Result<T, E>`?

---

`map()` transforms the success value if the Result is `Ok`, leaving `Err` unchanged:

```rust
let result: Result<i32, &str> = Ok(10);
let doubled = result.map(|x| x * 2);  // Ok(20)

let error: Result<i32, &str> = Err("failed");
let still_error = error.map(|x| x * 2);  // Err("failed")
```

It only applies the function to the `Ok` value.


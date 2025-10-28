## Converting Result To Option

How do you convert between `Result<T, E>` and `Option<T>`?

---

**Result to Option:**
```rust
let result: Result<i32, &str> = Ok(42);
let opt = result.ok();  // Some(42)

let err_result: Result<i32, &str> = Err("failed");
let opt = err_result.ok();  // None
```

**Option to Result:**
```rust
let opt: Option<i32> = Some(42);
let result = opt.ok_or("No value");  // Ok(42)

let none: Option<i32> = None;
let result = none.ok_or("No value");  // Err("No value")
```


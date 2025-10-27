## Copied And Cloned Methods

What's the difference between `copied()` and `cloned()` on `Option<&T>`?

---

Both convert `Option<&T>` to `Option<T>` by obtaining ownership:

`copied()`: Only works when `T: Copy` (types that can be copied bitwise)
```rust
let opt_ref: Option<&i32> = Some(&5);
let opt_owned: Option<i32> = opt_ref.copied();  // Some(5)
```

`cloned()`: Works when `T: Clone` (may allocate/do expensive work)
```rust
let opt_ref: Option<&String> = Some(&String::from("hi"));
let opt_owned: Option<String> = opt_ref.cloned();  // Some("hi")
```

Use `copied()` when possible (it's more efficient).


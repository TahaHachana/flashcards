## Result As Ref Pattern

How do you work with a Result without consuming it using `as_ref()`?

---

Use `as_ref()` to convert `Result<T, E>` to `Result<&T, &E>`:

```rust
let result = Ok(String::from("hello"));

// This consumes result
// let len = result.map(|s| s.len());

// This keeps result usable
let len = result.as_ref().map(|s| s.len());
println!("{:?}", result);  // Still usable: Ok("hello")
println!("{:?}", len);     // Some(5)
```

Similar to `Option`, use `as_ref()` when you need to inspect the value without taking ownership.


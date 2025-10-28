## Unwrap With Ownership

How does ownership work with `unwrap()` and what if you need to keep the original?

---

`unwrap()` and `expect()` consume (take ownership of) the `Result`/`Option`:

```rust
let result = Ok(42);
let value = result.unwrap();  // result is moved
// Can't use result anymore
```

**If you need to keep the original:**
```rust
let result = Ok(42);
let value = result.as_ref().unwrap();  // Borrows, doesn't move
println!("{:?}", result);  // Still usable: Ok(42)
```

Or use pattern matching:
```rust
let result = Ok(42);
match &result {
    Ok(v) => println!("Value: {}", v),
    Err(e) => println!("Error: {}", e),
}
println!("{:?}", result);  // Still usable
```


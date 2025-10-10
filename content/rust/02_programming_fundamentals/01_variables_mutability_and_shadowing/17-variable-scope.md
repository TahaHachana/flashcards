## Variable Scope

When is a variable valid in Rust?

---

From the point it's declared until the end of its scope (closing brace). Outside its scope, the variable is invalid.

```rust
{
    let x = 5;            // x valid from here
    println!("{}", x);    // x valid
}                          // x no longer valid
```


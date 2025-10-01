## Variable Scope

How does scope affect variable validity in Rust?

---

Variables are valid from declaration until their scope ends.  
When scope ends, the variable is dropped automatically.

```rust
{
    let s = "hello";
} // s is no longer valid
```


## If Expressions

What type must conditions in Rust `if` expressions evaluate to?

---

Conditions must always evaluate to a **bool**.  
Rust does not allow implicit conversions from integers or other types.

```rust
if number < 5 {
    println!("true");
}
```


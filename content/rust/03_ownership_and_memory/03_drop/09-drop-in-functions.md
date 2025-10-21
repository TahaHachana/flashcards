## Drop in Functions

When is a value dropped if passed to a function?

---

When the function ends. The function takes ownership and drops the value when it goes out of scope.

```rust
fn take(s: String) {
    println!("{}", s);
}  // s dropped here
```


## Returning References to Local Variables

Why does this code fail to compile, and what's the solution?
```rust
fn dangle<'a>() -> &'a String {
    let s = String::from("hello");
    &s
}
```

---

This fails because `s` is owned locally and dropped at the end of the function, creating a dangling reference. Lifetime annotations can't make data live longer than its scope. The solution is to return owned data instead:
```rust
fn no_dangle() -> String {
    String::from("hello")  // Ownership transferred
}
```


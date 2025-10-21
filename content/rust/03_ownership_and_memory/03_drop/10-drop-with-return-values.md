## Drop with Return Values

What happens to drop when a function returns a value?

---

Ownership transfers to caller, preventing drop. The returned value is NOT dropped in the function.

```rust
fn create() -> String {
    let s = String::from("hello");
    s  // Ownership moves out, NOT dropped here
}
```


## Ownership Return Values

What happens to ownership when a function returns a value?

---

Ownership transfers to the caller. The returned value's ownership moves out of the function to whoever receives it.

```rust
fn give() -> String {
    String::from("hello")  // Ownership moves to caller
}
let s = give();  // s now owns the string
```


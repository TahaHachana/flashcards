## Shadowing Vs Mut

What is the difference between shadowing and using `mut`?

---

* `mut` allows changing the **value** of the same variable, but not its type.
* Shadowing creates a new variable, which can even have a different type.

```rust
fn main() {
    let mut a = 5;
    a = 6; // ✅ same type, new value

    let spaces = "   ";
    let spaces = spaces.len(); // ✅ shadowed with new type (usize)
}
```


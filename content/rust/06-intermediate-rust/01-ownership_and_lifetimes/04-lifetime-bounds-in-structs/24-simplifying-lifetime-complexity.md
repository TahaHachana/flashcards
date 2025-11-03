## Simplifying Lifetime Complexity

What's the guideline for choosing between single and multiple lifetime parameters in structs?

---

Prefer single lifetime when possible:
```rust
struct Simple<'a> {
    field1: &'a str,
    field2: &'a str,
}
```
Use multiple only when fields actually have different lifetimes:
```rust
struct Complex<'a, 'b> {
    short: &'a str,
    long: &'b str,
}
```
Or consider owned data for simplicity (no lifetime parameters). Single lifetime is usually sufficient and much easier to work with.


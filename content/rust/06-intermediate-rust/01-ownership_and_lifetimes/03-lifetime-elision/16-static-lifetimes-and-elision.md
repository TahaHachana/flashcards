## Static Lifetimes and Elision

Can `'static` lifetimes be elided?

---

No, `'static` is special and must be written explicitly when part of a return type:
```rust
fn get_constant() -> &'static str {
    "hello, world"
}
```
However, string/byte literals and constants have implicit `'static` lifetimes:
```rust
const GREETING: &str = "hello";  // Implicit 'static
```


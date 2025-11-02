## Lifetimes as Generic Parameters

How are lifetime parameters similar to generic type parameters?

---

Lifetimes are generic parameters, just like types. They're declared similarly and can be combined:
```rust
fn example<'a, T>(x: &'a T) -> &'a T { x }
//         ^^  ^   lifetime  type
```
Both are compile-time abstractions that the compiler monomorphizes. You can have lifetime bounds just like trait bounds.


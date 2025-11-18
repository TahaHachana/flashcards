## Object-Safe Examples

Identify which traits are object-safe and which are not:

```rust
trait A {
    fn method(&self);
}

trait B {
    fn method<T>(&self);
}

trait C {
    fn method(&self) -> Self;
}

trait D {
    fn create() -> Self;
}
```

---

**Object-safe**:
- `A` ✅ - Method with `&self`, no problems

**NOT object-safe**:
- `B` ❌ - Generic method
- `C` ❌ - Returns `Self`
- `D` ❌ - Associated function without `self` that returns `Self`

Only trait `A` can be used as `Box<dyn A>`.


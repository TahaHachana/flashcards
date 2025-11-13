## Generic Type Without Declaration Error

What error do you get if you use a generic type without declaring it?

---

The compiler treats it as a concrete type and reports it can't be found:

```rust
// ❌ WRONG: T not declared
fn process(value: T) -> T {
    value
}
// Error: cannot find type `T` in this scope
```

**Solution**: Declare the generic parameter:

```rust
// ✅ CORRECT
fn process<T>(value: T) -> T {
    value
}
```

Generic parameters must be declared in angle brackets after the function/struct name.


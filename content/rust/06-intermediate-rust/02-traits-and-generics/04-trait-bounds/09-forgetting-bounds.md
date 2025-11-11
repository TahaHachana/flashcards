## Common Trait Bound Mistake

What error do you get if you try to use operations on a generic type without the proper trait bound?

---

You get a compiler error saying the operation cannot be applied:

```rust
fn compare<T>(a: T, b: T) -> bool {
    a > b  // ❌ Error: binary operation `>` cannot be applied to type `T`
}
```

**Solution**: Add the required trait bound:

```rust
fn compare<T: PartialOrd>(a: T, b: T) -> bool {
    a > b  // ✅ Works: T implements PartialOrd
}
```

The error message usually tells you which trait is needed.


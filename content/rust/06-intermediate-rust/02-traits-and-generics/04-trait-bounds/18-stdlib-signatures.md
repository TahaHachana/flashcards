## Reading Standard Library Signatures

How does understanding trait bounds help you read standard library function signatures?

---

Standard library functions use trait bounds extensively. Understanding them helps you know what types you can pass:

```rust
// From std library
pub fn max<T: Ord>(v1: T, v2: T) -> T {
    if v1 > v2 { v1 } else { v2 }
}
```

Reading this signature tells you:

- `T` can be any type
- `T` must implement `Ord` (total ordering)
- You can compare `T` values with `>`
- Function returns the same type `T`

The trait bounds document the requirements clearly.


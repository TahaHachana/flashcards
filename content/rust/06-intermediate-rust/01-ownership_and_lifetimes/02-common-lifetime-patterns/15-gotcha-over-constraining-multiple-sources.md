## Gotcha Over-Constraining Multiple Sources

What's the problem with this signature, and how would you fix it?

```rust
fn find_or_default<'a>(
    data: &'a [i32],
    target: i32,
    default: &'a i32
) -> &'a i32
```

---

Too restrictive—it forces `default` to have the same lifetime as `data` and the return value, even though the return never uses `default` when a match is found. Fix by using independent lifetimes:
```rust
fn find_or_default<'a, 'b>(
    data: &'a [i32],
    target: i32,
    default: &'b i32
) -> &'a i32
```
This allows `default` to have a different (shorter) lifetime.


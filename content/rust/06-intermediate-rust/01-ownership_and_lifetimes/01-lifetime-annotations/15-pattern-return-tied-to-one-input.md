## Pattern Return Tied to One Input

When should you use different lifetimes for different parameters?

---

Use different lifetimes when the return clearly comes from one specific input:
```rust
fn get_first<'a>(values: &'a [i32], _default: &i32) -> &'a i32 {
    &values[0]
}
```
Here the return is tied only to `values`, not `_default`, so `_default` can have an independent (potentially shorter) lifetime.


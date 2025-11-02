## Pattern All Parameters Share Lifetime

When should you use the same lifetime `'a` for all parameters and the return value?

---

Use the same lifetime when the return value could come from any of the inputs, so all must live long enough. Example:
```rust
fn pick_one<'a>(x: &'a i32, y: &'a i32, condition: bool) -> &'a i32 {
    if condition { x } else { y }
}
```
This ensures both inputs remain valid for as long as the output is used.


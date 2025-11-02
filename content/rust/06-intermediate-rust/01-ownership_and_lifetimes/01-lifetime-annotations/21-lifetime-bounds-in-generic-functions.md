## Lifetime Bounds in Generic Functions

Why might you need a lifetime bound like `T: 'a` in a generic function?

---

You need `T: 'a` when a generic type `T` might contain references that need to live at least as long as `'a`:
```rust
fn print_ref<'a, T>(x: &'a T)
where
    T: Display + 'a  // T must live at least as long as 'a
{
    println!("{}", x);
}
```
This ensures any references inside `T` remain valid for the duration of `'a`.


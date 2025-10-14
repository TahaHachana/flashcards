## Call by Value

What happens when you pass a Copy type to a function?

---

The value is copied. Modifications inside the function don't affect the original.

```rust
fn modify(mut x: i32) {
    x = 10;  // Only modifies local copy
}
let num = 5;
modify(num);
println!("{}", num);  // Still 5
```


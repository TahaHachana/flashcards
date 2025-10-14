## Call by Reference

How do you allow a function to modify the original value?

---

Pass a mutable reference using &mut.

```rust
fn increment(x: &mut i32) {
    *x += 1;
}
let mut num = 5;
increment(&mut num);
println!("{}", num);  // 6
```


# Mutable References

How many mutable references (`&mut T`) can you have to the same data in one scope, and why?

---

Only one mutable reference per scope. This ensures exclusive write access and prevents data races.

```rust
let mut s = String::from("hi");
{
    let r1 = &mut s;
    r1.push('!');
} // r1 goes out of scope here
let r2 = &mut s;
r2.push('?');
println!("{}", s); // prints "hi!?"
```
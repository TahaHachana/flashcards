## Manual Dereferencing

When do you need to manually dereference with *?

---

To get the value a reference points to, or to modify through a mutable reference.

```rust
let x = 5;
let r = &x;
println!("{}", *r);  // Get value

let r = &mut x;
*r = 10;  // Modify value
```


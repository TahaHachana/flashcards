## Ownership During Iteration

What's wrong with this code?
```rust
let vec = vec![String::from("hello")];
for item in vec {
    println!("{}", item);
}
println!("{:?}", vec);
```

---

The for loop consumes the vector (calls `.into_iter()`), moving ownership of each String. After the loop, `vec` no longer exists. Fix: Use `for item in &vec` to borrow instead.


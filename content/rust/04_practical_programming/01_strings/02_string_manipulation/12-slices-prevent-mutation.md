## Slices Prevent Mutation

Why does this code produce an error?
```rust
let mut s = String::from("hello world");
let word = &s[0..5];
s.clear();
println!("{}", word);
```

---

The immutable slice (word) prevents mutation of the source. While word exists as an immutable borrow, you cannot borrow s mutably (which clear() requires). This prevents use-after-free bugs where the slice would reference cleared/invalid data. Rust's borrow checker enforces this at compile time.


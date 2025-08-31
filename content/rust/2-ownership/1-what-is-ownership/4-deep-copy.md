# Deep Copy with Clone

How do you perform a deep copy of heap data in Rust?

---

Call `.clone()` to allocate new heap memory and duplicate the contents.

```rust
let s1 = String::from("hello");
let s2 = s1.clone();
println!("s1 = {}, s2 = {}", s1, s2); // both valid
```
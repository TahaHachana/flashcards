## Slicing is Borrowing

After creating a slice, can you still use the original String? Why or why not?

---

Yes, both remain valid:
```rust
let s = String::from("hello world");
let hello = &s[0..5];

println!("{}", hello);  // Can use slice
println!("{}", s);      // Original still valid
```
The slice borrows from the String - it's an immutable reference. The original String hasn't been moved or modified, just borrowed.


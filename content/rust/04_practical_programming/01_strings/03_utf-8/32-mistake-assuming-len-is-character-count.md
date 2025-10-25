## Mistake - Assuming len is Character Count

What's wrong with this assumption and how do you fix it?
```rust
let s = String::from("你好");
println!("{}", s.len());  // Assuming this is character count
```

---

```rust
let s = String::from("你好");
println!("{}", s.len());  // 6 bytes, not 2 characters!

// For character count:
println!("{}", s.chars().count());  // 2 characters
```
len() returns bytes, not characters. Always use chars().count() for character count.


## Mistake - Comparing String Lengths

What's wrong with this comparison?
```rust
let s1 = String::from("hello");
let s2 = String::from("你好");
if s1.len() > s2.len() {
    println!("s1 has more characters");
}
```

---

```rust
// ❌ Wrong: s1 has 5 bytes, s2 has 6 bytes
// But s1 has 5 chars, s2 has 2 chars
if s1.len() > s2.len() {
    println!("s1 has more characters");
}

// ✅ Correct: compare character counts
if s1.chars().count() > s2.chars().count() {
    println!("s1 has more characters");
}
```
len() compares bytes, not characters. Use chars().count() for character comparison.


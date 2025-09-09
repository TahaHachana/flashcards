# String Slice Syntax

How do you create a string slice from a `String`?

---

Use range notation on a `String` reference with optional start or end indices:

```rust
fn main() {
    let s = String::from("hello");
    let part1 = &s[0..2]; // "he"
    let part2 = &s[2..];  // "llo"
    let whole = &s[..];   // "hello"
    println!("{}, {}, {}", part1, part2, whole);
}
```
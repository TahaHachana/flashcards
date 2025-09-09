# Slice Range Shorthand

What shorthand forms exist for slicing with ranges?

---

- `&s[..end]` is equivalent to `&s[0..end]`  
- `&s[start..]` is equivalent to `&s[start..s.len()]`  
- `&s[..]` takes a full slice of the entire collection  

```rust
fn main() {
    let s = String::from("rustacean");
    println!("{}", &s[..4]); // "rust"
    println!("{}", &s[4..]); // "acean"
}
```
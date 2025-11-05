## Display and ToString Relationship

If you implement `Display` for your type, do you need to implement `ToString` as well?

---

No! You should NOT implement `ToString` manually. When you implement `Display`, you automatically get `ToString` for free through a blanket implementation in the standard library.

```rust
// ✅ CORRECT: Only implement Display
impl Display for MyType {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "MyType")
    }
}

fn main() {
    let m = MyType;
    let s = m.to_string();  // to_string() works automatically!
}
```


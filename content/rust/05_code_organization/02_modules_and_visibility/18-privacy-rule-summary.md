## Rust's Privacy Rule Summary

What is Rust's official rule about default privacy and its exceptions?

---

**The rule**: "By default, everything is private, with two exceptions: items in a `pub` trait are public by default; enum variants in a `pub` enum are also public by default."

**Breaking it down**:

**Private by default**:
- Functions, structs, fields, modules, etc. all start private
- Must explicitly use `pub` to make accessible

**Exception 1 - Traits**:
```rust
pub trait Drawable {
    fn draw(&self);  // Automatically public
}
```

**Exception 2 - Enums**:
```rust
pub enum Color {
    Red,    // Automatically public
    Green,  // Automatically public
    Blue,   // Automatically public
}
```


## The use super::*; Pattern

Why is `use super::*;` needed in test modules and what does it import?

---

Test modules are child modules that can't access parent items by default.

`use super::*;` imports all public items from the parent:
- `super` refers to the parent module
- `*` imports all public items

What gets imported:
```rust
pub fn public_fn() {}        // ✓ Imported
fn private_fn() {}           // ✗ Not imported
pub struct PublicStruct {}   // ✓ Imported
const CONST: i32 = 10;       // ✗ Not imported (needs pub)
```

Example:
```rust
#[cfg(test)]
mod tests {
    use super::*;  // Import parent's public items
    
    #[test]
    fn test() {
        public_fn();  // Now accessible
    }
}
```


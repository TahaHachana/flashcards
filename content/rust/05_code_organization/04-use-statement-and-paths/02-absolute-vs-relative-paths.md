## Absolute vs Relative Paths

What is the difference between absolute and relative paths in Rust?

---

**Absolute paths**: Start from the crate root or external crate name
```rust
crate::front_of_house::hosting::add_to_waitlist();
std::collections::HashMap::new();
rand::thread_rng();
```

**Relative paths**: Start from current location
```rust
mod parent {
    pub fn helper() {}
    
    pub mod child {
        pub fn work() {
            super::helper();  // Relative - go up one level
        }
    }
}
```

**When to use**:
- **Absolute**: For clarity, when referencing from crate root, external crates
- **Relative**: For convenience within nested modules


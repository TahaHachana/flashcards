## Declaring and Using Basic Modules

How do you declare a module in Rust, and what's the key principle about module scope?

---

**Declaration**:
```rust
mod module_name {
    // Module contents
}
```

**Key principle**: Modules are separate spaces (separate namespaces).

**Implications**:
- Each module needs its own imports (`use` statements)
- Items inside don't automatically see items outside
- Items are private by default and need `pub` to be accessible from outside

Example:
```rust
mod printer {
    use std::fmt::Display;  // Import needed inside module
    
    pub fn print<T: Display>(item: T) {
        println!("{}", item);
    }
}
```


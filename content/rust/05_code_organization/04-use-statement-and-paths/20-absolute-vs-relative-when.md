## Absolute vs Relative Paths - When to Use

When should you use absolute paths vs relative paths?

---

**Use absolute paths (`crate::`)** when:
- You want to be explicit about full path
- Referencing items from different parts of module tree
- Code might move and you want paths to stay valid

**Use relative paths (`super::`, `self::`)** when:
- Accessing parent or sibling modules
- Staying within a local area of the module tree
- Shorter paths improve readability

**Example comparison**:
```rust
mod parent {
    pub fn helper() {}
    
    pub mod child {
        pub fn work() {
            // Absolute (explicit)
            crate::parent::helper();
            
            // Relative (concise)
            super::helper();
            
            // Both work - choose based on context
        }
    }
}
```

**Guideline**: Use relative for nearby modules, absolute when reaching across the crate.


## Test Module Import Pattern

What is the common pattern for imports in test modules?

---

**Pattern**: Use `use super::*;` to import everything from the parent module.

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn helper(x: i32) -> i32 {  // Private function
    x * 2
}

#[cfg(test)]
mod tests {
    use super::*;  // Import all from parent
    
    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }
    
    #[test]
    fn test_helper() {
        assert_eq!(helper(3), 6);  // Can test private functions!
    }
}
```

**Why this works**: Test modules are children of the code they test, so they can access private items.

**`use super::*`** = "import everything from parent module"


## Forgetting use super::* Error

What error occurs when you forget `use super::*;` in a test module?

---

Without `use super::*;`, test functions cannot find parent module items:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    // Missing: use super::*;
    
    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
        // Error: cannot find function `add` in this scope
    }
}
```

Solution:
```rust
#[cfg(test)]
mod tests {
    use super::*;  // Import parent items
    
    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);  // Works!
    }
}
```


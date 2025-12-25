## Testing Edge Cases

What types of edge cases should you test and why?

---

Always test boundary conditions and unusual inputs:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_empty_input() {
        assert_eq!(count_words(""), 0);
    }
    
    #[test]
    fn test_single_element() {
        assert_eq!(count_words("hello"), 1);
    }
    
    #[test]
    fn test_typical_case() {
        assert_eq!(count_words("hello world"), 2);
    }
    
    #[test]
    fn test_extra_whitespace() {
        assert_eq!(count_words("  hello   world  "), 2);
    }
}
```

Categories:
- Empty/null inputs
- Single element
- Boundary values (min/max)
- Invalid formats
- Whitespace handling

Edge cases often reveal bugs that typical inputs miss.


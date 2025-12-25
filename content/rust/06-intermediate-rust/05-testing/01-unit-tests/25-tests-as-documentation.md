## Tests as Documentation

How do tests serve as documentation in Rust?

---

Tests demonstrate how to use APIs through working examples:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn example_basic_usage() {
        // Shows how to create and use the type
        let parser = Parser::new();
        let result = parser.parse("42");
        assert_eq!(result, Some(42));
    }
    
    #[test]
    fn example_error_handling() {
        // Shows what happens with invalid input
        let parser = Parser::new();
        let result = parser.parse("invalid");
        assert_eq!(result, None);
    }
}
```

Benefits:
- Shows real usage patterns
- Examples are guaranteed to compile and work
- Updates automatically when APIs change
- Demonstrates edge cases and error handling

Tests complement doc comments by providing executable examples.


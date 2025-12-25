## Parametrized Test Pattern

How do you implement parametrized tests manually in Rust?

---

Create helper function called from test with multiple inputs:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    fn test_parse_case(input: &str, expected: i32) {
        let result = parse(input);
        assert_eq!(
            result, expected,
            "Failed for input: '{}'", input
        );
    }
    
    #[test]
    fn test_parse_various_inputs() {
        // Multiple test cases in one test
        test_parse_case("0", 0);
        test_parse_case("42", 42);
        test_parse_case("-10", -10);
        test_parse_case("999", 999);
    }
    
    #[test]
    fn test_parse_errors() {
        assert!(parse("abc").is_err());
        assert!(parse("").is_err());
        assert!(parse("12.34").is_err());
    }
}
```

Benefits: Many cases in one test, clear failure messages showing which case failed.

Alternative: External crates like `rstest` for macro-based parametrization.


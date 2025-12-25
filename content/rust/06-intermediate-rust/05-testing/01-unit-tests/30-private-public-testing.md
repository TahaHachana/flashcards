## Private vs Public Testing Strategy

What is the recommended strategy for deciding whether to test private or public functions?

---

Strategy:

1. **Prefer testing public APIs**:
```rust
pub fn process_data(input: &str) -> Result<Data, Error> {
    let parsed = parse_internal(input)?;
    validate_internal(&parsed)?;
    Ok(transform_internal(parsed))
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_process_data() {
        // Test the public function
        let result = process_data("input");
        assert!(result.is_ok());
    }
}
```

2. **Test private functions when**:
- Logic is complex and deserves isolated testing
- Public API doesn't adequately exercise the function
- Function is critical and has many edge cases

```rust
fn complex_algorithm(data: &[i32]) -> i32 {
    // Complex logic worth testing directly
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_complex_algorithm_directly() {
        assert_eq!(complex_algorithm(&[1, 2, 3]), 6);
    }
}
```

Philosophy: Public APIs are your contract; private functions are implementation details.


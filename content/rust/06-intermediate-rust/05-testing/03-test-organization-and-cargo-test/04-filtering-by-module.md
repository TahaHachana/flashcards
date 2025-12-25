## Filtering by Module Path

How do you run tests in a specific module?

---

Use the module path as a filter:

```bash
# Run tests in 'calculator' module
cargo test calculator

# Run tests in nested modules
cargo test tests::math::addition
```

Example:
```rust
#[cfg(test)]
mod tests {
    mod calculator {
        #[test]
        fn test_add() { }
        
        #[test]
        fn test_subtract() { }
    }
    
    mod parser {
        #[test]
        fn test_parse() { }
    }
}
```

```bash
$ cargo test calculator
running 2 tests
test tests::calculator::test_add ... ok
test tests::calculator::test_subtract ... ok
```

This runs all tests within the specified module.


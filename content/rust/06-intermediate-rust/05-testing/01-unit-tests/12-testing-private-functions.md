## Testing Private Functions

Can unit tests in the same file test private (non-pub) functions? Why or why not?

---

Yes, unit tests in the same file can test private functions.

The test module is a child module within the same file, so it has access to private items:

```rust
// Private function
fn internal_calculation(x: i32) -> i32 {
    x * 2 + 1
}

pub fn public_api(x: i32) -> i32 {
    internal_calculation(x)
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_internal() {
        // Can test private function
        assert_eq!(internal_calculation(5), 11);
    }
}
```

Philosophy: Test through public APIs when possible, but testing private functions for complex logic is acceptable.


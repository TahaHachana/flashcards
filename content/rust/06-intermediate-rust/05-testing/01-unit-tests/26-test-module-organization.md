## Test Module Organization

How can you organize tests into sub-modules for better structure?

---

Create nested modules within the test module:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    mod addition {
        use super::*;
        
        #[test]
        fn test_positive() {
            assert_eq!(add(2, 2), 4);
        }
        
        #[test]
        fn test_negative() {
            assert_eq!(add(-2, -2), -4);
        }
    }
    
    mod multiplication {
        use super::*;
        
        #[test]
        fn test_by_zero() {
            assert_eq!(multiply(5, 0), 0);
        }
    }
}
```

Test output shows hierarchy:
```
test tests::addition::test_positive ... ok
test tests::multiplication::test_by_zero ... ok
```


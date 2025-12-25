## Test Organization by Type

How can you organize tests by type (unit, integration, edge cases) within a test module?

---

Create sub-modules for different test types:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    mod unit {
        use super::*;
        
        #[test]
        fn test_pure_function() { }
        
        #[test]
        fn test_calculation() { }
    }
    
    mod integration {
        use super::*;
        
        #[test]
        fn test_components_together() { }
        
        #[test]
        fn test_full_workflow() { }
    }
    
    mod edge_cases {
        use super::*;
        
        #[test]
        fn test_empty_input() { }
        
        #[test]
        fn test_overflow() { }
    }
}
```

Run specific types:
```bash
cargo test unit
cargo test edge_cases
cargo test integration
```

Benefits: Clear categorization, selective execution.


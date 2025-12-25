## Test Organization by Feature

How should you organize tests by feature in your test module?

---

Group tests in sub-modules by feature:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    mod authentication {
        use super::*;
        
        #[test]
        fn test_login() { }
        
        #[test]
        fn test_logout() { }
        
        #[test]
        fn test_session_expiry() { }
    }
    
    mod database {
        use super::*;
        
        #[test]
        fn test_connection() { }
        
        #[test]
        fn test_query() { }
    }
}
```

Run specific feature tests:
```bash
cargo test authentication  # Only auth tests
cargo test database        # Only database tests
```

Benefits: Logical organization, selective execution, clear structure.


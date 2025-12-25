## Purpose of #[cfg(test)] Module

Why use `#[cfg(test)]` to wrap test modules instead of just using `#[test]` on individual functions?

---

`#[cfg(test)]` provides conditional compilation:

Benefits:
1. Code inside is **only compiled** during `cargo test`
2. Not included in release builds → reduces binary size
3. Keeps tests close to implementation without polluting public API
4. Can contain helper functions shared across tests

Example:
```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_one() { }
    
    #[test]
    fn test_two() { }
}
```

Without `#[cfg(test)]`, test code would ship in production binaries.


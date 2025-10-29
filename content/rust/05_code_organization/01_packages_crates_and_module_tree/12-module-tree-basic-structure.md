## Module Tree Basic Structure

How do you define a basic module tree structure in Rust? Provide an example.

---

```rust
// In src/lib.rs or src/main.rs (crate root)

mod network {
    mod server {
        fn connect() {
            // Implementation
        }
    }
    
    mod client {
        fn connect() {
            // Implementation
        }
    }
}

mod authentication {
    fn login() {
        // Implementation
    }
}
```

This creates a tree:
```
crate (root)
  ├── network
  │     ├── server
  │     └── client
  └── authentication
```


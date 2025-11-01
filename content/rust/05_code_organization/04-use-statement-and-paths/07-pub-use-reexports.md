## Pub Use for Re-exports

What is `pub use`, and why would you use it?

---

**`pub use`**: Re-exports items at a different path, making them accessible to external users.

**Problem**: Deep nesting creates long paths
```rust
// Internal structure
mod internal {
    pub mod deeply {
        pub mod nested {
            pub struct Helper {}
        }
    }
}

// Users must write:
use my_crate::internal::deeply::nested::Helper;  // Verbose!
```

**Solution**: Re-export with `pub use`
```rust
pub use internal::deeply::nested::Helper;

// Users can now write:
use my_crate::Helper;  // Clean!
```

**Benefits**:
- Simplify API for users
- Hide internal organization
- Create logical groupings at crate root


## Public API with Private Implementation

What is the benefit of exposing a public API while keeping implementation details private?

---

**Benefit**: You can change internal implementation without breaking external code.

**Example**:
```rust
pub mod database {
    pub struct Database {
        connection: Connection,  // Private implementation
    }
    
    impl Database {
        pub fn new(url: &str) -> Result<Self, Error> {
            // Public interface
        }
        
        pub fn query(&self, sql: &str) -> Result<Vec<Row>, Error> {
            // Public interface
        }
    }
    
    struct Connection {  // Private helper
        // Can change this freely
    }
}
```

**What users see**: Only `Database`, `new()`, and `query()`
**What you can change freely**: Anything about `Connection` or internal implementation

**This is encapsulation** - hide complexity, expose simplicity.


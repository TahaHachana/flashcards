## Constructing Structs with Private Fields

If a struct's fields are private, how can external code create instances of it?

---

**Problem**: Can't use struct literal syntax if fields are private.

**Solution**: Provide a public constructor (typically `new`):

```rust
pub struct User {
    name: String,      // Private
    email: String,     // Private
}

impl User {
    pub fn new(name: String, email: String) -> Self {
        Self { name, email }  // Constructor can access private fields
    }
}

// Usage:
let user = User::new("Alice".to_string(), "alice@example.com".to_string());
```

**Alternative patterns**:
- Builder pattern for many fields
- `Default` implementation
- Factory methods with validation


## Items Must Be Public to Import

Can you use `use` to import private items from another module?

---

**No** - you can only `use` items that are visible to you.

**Example of error**:
```rust
mod network {
    struct Connection {}  // Private!
}

use network::Connection;  // ERROR: Connection is private
```

**Fix**: Make the item public
```rust
mod network {
    pub struct Connection {}  // Public!
}

use network::Connection;  // Works!
```

**Exception**: Child modules can access parent's private items
```rust
mod parent {
    struct Private {}  // Private
    
    mod child {
        use super::Private;  // OK - child can access parent's private items
    }
}
```

**Rule**: Visibility restrictions apply to `use` statements, except for child modules accessing parent items.


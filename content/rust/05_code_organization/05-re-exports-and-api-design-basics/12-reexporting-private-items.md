## Re-exporting Private Items Error

Can you re-export an item that isn't marked `pub`? What happens?

---

**No** - you cannot re-export private items.

**Error**:
```rust
mod internal {
    struct Helper {}  // Not pub!
}

pub use internal::Helper;  // ERROR: Helper is private
```

**Compiler error**: "struct `Helper` is private"

**Fix**: Make the original item public
```rust
mod internal {
    pub struct Helper {}  // Now pub
}

pub use internal::Helper;  // Works!
```

**Rule**: To re-export something with `pub use`, the original item must be `pub` in its declaring module.

**Rationale**: Can't make something more visible than its original visibility.


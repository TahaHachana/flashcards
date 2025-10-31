## Private Module Makes Public Items Inaccessible

What's wrong with this code, and how do you fix it?

```rust
mod internal {           
    pub struct Helper {  
        pub value: i32,
    }
}

fn main() {
    let h = internal::Helper { value: 42 };
}
```

---

**Problem**: The module `internal` itself is private, so even though `Helper` is public, you can't access it from outside.

**Error**: `module 'internal' is private`

**Fix**: Make the module public:
```rust
pub mod internal {       // Module is now accessible
    pub struct Helper {
        pub value: i32,
    }
}

fn main() {
    let h = internal::Helper { value: 42 };  // Works!
}
```

**Rule**: Both the module AND the item must be public for external access.


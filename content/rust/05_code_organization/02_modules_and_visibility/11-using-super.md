## Using Super to Navigate Up Module Tree

What does `super::` do, and how do you use it to access items in parent modules?

---

**`super::`** moves up one level in the module tree (to the parent module).

**Usage**:
```rust
mod parent {
    fn parent_function() {}
    
    pub mod child {
        fn child_function() {
            super::parent_function();        // One level up
        }
        
        pub mod grandchild {
            fn grandchild_function() {
                super::child_function();           // One level up
                super::super::parent_function();   // Two levels up
            }
        }
    }
}
```

**Alternative**: Use `crate::` to start from the root:
```rust
crate::parent::parent_function();  // Absolute path from root
```


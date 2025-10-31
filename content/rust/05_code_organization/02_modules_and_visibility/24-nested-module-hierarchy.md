## Nested Module Visibility Hierarchy

How does visibility work in a hierarchy of nested modules? Can outer modules access inner module items?

---

**Rule**: Children can always access parent items, but parents CANNOT access child items unless they're public.

**Example**:
```rust
mod outer {
    fn outer_fn() {}
    
    mod inner {
        fn inner_fn() {
            super::outer_fn();  // OK - child accessing parent
        }
    }
    
    fn another_outer_fn() {
        // inner::inner_fn();  // ERROR - parent can't access private child
    }
}
```

**Mental model**: Think like geography
- A city (child) is always in its country (parent) - child sees parent
- A country (parent) might not know about every private street in a city - parent doesn't see private children

**To allow parent access**: Make child items public:
```rust
mod inner {
    pub fn inner_fn() {}  // Now parent can access
}
```


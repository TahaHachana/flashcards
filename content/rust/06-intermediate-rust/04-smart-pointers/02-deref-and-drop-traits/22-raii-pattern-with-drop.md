## RAII Pattern with Drop

What is the RAII pattern, and how does `Drop` enable it in Rust?

---

**RAII (Resource Acquisition Is Initialization):** Resources are acquired in a constructor and automatically released in a destructor.

**How Drop enables RAII:**
```rust
struct Guard<'a> {
    resource: &'a mut Resource,
}

impl<'a> Guard<'a> {
    fn new(resource: &'a mut Resource) -> Self {
        resource.acquire();  // Acquire in constructor
        Guard { resource }
    }
}

impl Drop for Guard<'_> {
    fn drop(&mut self) {
        self.resource.release();  // Release in destructor
    }
}

// Usage
{
    let mut resource = Resource::new();
    let _guard = Guard::new(&mut resource);
    // Use resource safely
}  // Guard dropped, resource automatically released
```

**Benefits:**
- Guaranteed cleanup even if panic occurs
- Impossible to forget to release resources
- Scope-based resource management

**Examples in std:** `MutexGuard`, `File`, `JoinHandle`


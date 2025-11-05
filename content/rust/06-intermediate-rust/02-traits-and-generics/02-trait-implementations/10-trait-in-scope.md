## Trait Must Be in Scope

Why might you get a "method not found" error even though your type implements a trait? What's the solution?

---

The trait must be in scope (imported) to use its methods, even if the type implements it.

**Problem**:
```rust
fn main() {
    let logger = MyLogger;
    logger.log("Hi");  // Error: method not found
}
```

**Solution**: Import the trait
```rust
use my_crate::Logger;  // Bring trait into scope

fn main() {
    let logger = MyLogger;
    logger.log("Hi");  // Now works!
}
```


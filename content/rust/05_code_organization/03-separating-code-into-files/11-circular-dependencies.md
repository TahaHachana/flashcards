## Circular Dependencies Problem

What is a circular dependency in modules, and how do you fix it?

---

**Problem**: Module A depends on Module B, which depends on Module A.

```rust
// src/a.rs
use crate::b::B;
pub struct A { b: B }

// src/b.rs
use crate::a::A;
pub struct B { a: A }  // Circular!
```

**Fixes**:

1. **Extract common types to shared module**:
```rust
// src/common.rs
pub struct SharedData {}

// Both A and B depend on common, no cycle
```

2. **Use trait objects or enums** instead of concrete types

3. **Use `Rc`/`Arc` with interior mutability** if truly needed

4. **Redesign**: Often indicates poor separation of concerns

**Best solution**: Usually redesign to avoid circularity.


## Circular Use Dependencies

What causes circular use dependencies, and how do you fix them?

---

**Circular dependency**: Module A uses items from Module B, which uses items from Module A.

**Problem**:
```rust
// src/a.rs
use crate::b::B;
pub struct A { b: B }

// src/b.rs
use crate::a::A;
pub struct B { a: A }  // Circular!
```

**Fixes**:

**1. Extract common code**:
```rust
// src/common.rs
pub struct SharedData {}

// src/a.rs
use crate::common::SharedData;

// src/b.rs
use crate::common::SharedData;
```

**2. Use trait objects** to break the cycle

**3. Redesign structure** to avoid dependency

**Best solution**: Usually indicates poor separation of concerns—redesign module boundaries.

**Note**: Circular `use` statements are different from circular module dependencies (which Rust prevents at compile time).


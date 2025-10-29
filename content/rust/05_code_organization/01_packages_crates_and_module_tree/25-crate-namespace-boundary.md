## Crate Forms a Namespace Boundary

How do crates function as namespace boundaries, and what does this mean for naming?

---

**Namespace boundary:**
- Each crate has its own namespace
- Two different crates can have items with the same name without conflict
- You qualify items with the crate name to distinguish them

**Example:**
```rust
use crate_a::Config;  // Config from crate_a
use crate_b::Config;  // Config from crate_b

// Use qualified paths to distinguish:
let config_a = crate_a::Config::new();
let config_b = crate_b::Config::new();
```

**Benefit:** You don't have to worry about naming conflicts with external dependencies—each crate is isolated.


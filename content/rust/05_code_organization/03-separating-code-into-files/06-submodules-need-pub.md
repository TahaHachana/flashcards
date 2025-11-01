## Submodules Need Pub to Be Accessible

Why does this code fail, and how do you fix it?

```rust
// src/network/mod.rs
mod server;

// src/main.rs
use my_lib::network::server;
```

---

**Problem**: The submodule `server` is private (declared with `mod` not `pub mod`).

**Error**: `module 'server' is private`

**Fix**: Make the submodule public:
```rust
// src/network/mod.rs
pub mod server;  // Now publicly accessible
```

**Key insight**:
- Just because `network` is public doesn't make its submodules public
- Each module declaration needs its own `pub` keyword
- This is consistent with Rust's "private by default" philosophy


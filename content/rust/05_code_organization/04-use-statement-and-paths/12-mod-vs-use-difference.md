## Mod vs Use - Critical Difference

What is the critical difference between `mod` and `use`?

---

**`mod`** - **Declares** a module (makes it exist)
**`use`** - **Imports** from an already-declared module

**Wrong order**:
```rust
use helper::function;  // ERROR: Can't find module `helper`
mod helper;            // Too late!
```

**Correct order**:
```rust
mod helper;            // Declare first
use helper::function;  // Then import
```

**Key insight**:
- `mod` tells Rust "this module exists"
- `use` tells Rust "bring this item into scope"
- You must declare before you can import

**Analogy**: `mod` creates the room, `use` puts furniture from that room into your current space.


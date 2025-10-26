## Enum Variant Namespace

How do you access enum variants in Rust, and what syntax error happens if you forget the namespace?

---

Enum variants are **namespaced under the enum name**:

```rust
enum Direction {
    North,
    South,
}

// WRONG
let dir = North;  // ERROR: can't find value `North`

// CORRECT
let dir = Direction::North;  // Must use EnumName::Variant
```

**Optional shortcut** - bring variants into scope:
```rust
use Direction::*;
let dir = North;  // Now OK
```

But use carefully to avoid naming conflicts. The `::` syntax makes the enum origin clear.


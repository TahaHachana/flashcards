## Path Keywords - Crate, Super, Self

What do the path keywords `crate::`, `super::`, and `self::` mean?

---

**`crate::`** - Start from the crate root
```rust
crate::database::connect();  // Like `/` in file systems
```

**`super::`** - Go up one module (parent)
```rust
super::parent_function();    // Like `../` in file systems
```

**`self::`** - Current module (often implicit)
```rust
self::my_function();         // Like `./` in file systems
use self::my_module::Item;   // Usually just: use my_module::Item;
```

**Mental model**:
- `crate::` = absolute path from root
- `super::` = go up the tree
- `self::` = stay at current level


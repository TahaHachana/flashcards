## File-to-Module Mapping

How does Rust map modules to files and folders?

---

Each `mod` declaration corresponds to a file or folder:

```rust
// src/main.rs
mod utils;
```

Maps to:

```
src/utils.rs
```

A folder module uses `mod.rs`:

```
src/network/
├── mod.rs
└── client.rs
```

`mod.rs` is the parent, exposing submodules.


## Path Resolution Relative to Declaring File

If you have nested modules, where does Rust look for submodule files?

---

**Rule**: Submodule paths are resolved **relative to the file containing the declaration**.

**Example**:
```rust
// src/lib.rs
mod network;
// Looks in: src/network.rs or src/network/mod.rs

// src/network.rs (or src/network/mod.rs)
pub mod server;
// Looks in: src/network/server.rs (relative to network.rs location)

pub mod client;
// Looks in: src/network/client.rs
```

**Parallel structure**:
```
src/
├── lib.rs           ← declares `mod network`
├── network.rs       ← declares `pub mod server`
└── network/
    └── server.rs    ← server submodule code
```

**NOT** relative to crate root!


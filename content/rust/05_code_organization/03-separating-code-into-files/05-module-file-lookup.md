## Where Rust Looks for Module Files

When you write `mod network;` in a file, where does Rust look for the module file?

---

**Rule**: Rust looks for modules **relative to the file containing the `mod` declaration**.

**Example**:
```rust
// In src/lib.rs
mod network;  
// Looks in src/ for:
// 1. src/network.rs
// 2. src/network/mod.rs

// In src/network/mod.rs
mod server;
// Looks in src/network/ for:
// 1. src/network/server.rs
// 2. src/network/server/mod.rs
```

**Common mistake**: Thinking Rust looks relative to the crate root
**Reality**: Looks relative to the declaring file

**NOT**: `src/lib/network.rs` (wrong!)


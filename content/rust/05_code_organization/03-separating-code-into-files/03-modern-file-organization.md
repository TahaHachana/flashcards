## Modern File Organization (Rust 2018+)

What is the modern (Rust 2018+) way to organize modules with submodules, and what are its advantages?

---

**Modern structure**: Use both a `.rs` file and a directory:
```
src/
├── lib.rs
├── network.rs          ← Module contents
└── network/
    ├── server.rs       ← Submodule
    └── client.rs       ← Submodule
```

```rust
// src/network.rs
pub mod server;  // Looks in network/server.rs
pub mod client;  // Looks in network/client.rs

pub fn init() {
    println!("Network initialized");
}
```

**Advantages**:
- No special `mod.rs` files needed
- More intuitive file structure
- Parallel file and directory can coexist
- Cleaner than old `network/mod.rs` pattern


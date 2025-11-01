## Critical Rule - Files Must Be Declared

What is the most critical rule about using multiple files in Rust, and what happens if you don't follow it?

---

**Rule**: Rust won't see or compile a `.rs` file unless you explicitly declare it with `mod`.

**What happens without declaration**:
- You can create `helper.rs`, write any code in it
- Your IDE might notice it, but the compiler completely ignores it
- The file doesn't exist as far as Rust is concerned
- No compilation errors about unused files

**To make Rust notice**:
```rust
// In src/lib.rs or src/main.rs
mod helper;  // Now Rust will look for and compile src/helper.rs
```

**Key insight**: Files don't automatically become modules—you must declare them.


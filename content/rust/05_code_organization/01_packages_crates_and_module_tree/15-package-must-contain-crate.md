## Package Must Contain at Least One Crate

What is the minimum requirement for a valid Rust package regarding crates?

---

A package must contain **at least one crate**—either a binary crate OR a library crate.

**Valid packages:**
- ✅ Just `src/main.rs` (one binary)
- ✅ Just `src/lib.rs` (one library)
- ✅ Both `src/main.rs` and `src/lib.rs`
- ✅ `src/lib.rs` + multiple files in `src/bin/`

**Invalid:**
- ❌ A package with only `Cargo.toml` and no source files


## Best Practices Summary

What are the key best practices for organizing code across multiple files in Rust?

---

**Best practices**:

1. **Always declare with `mod`**
- Files don't exist without explicit declaration

2. **Mirror structure**
- File organization should parallel module tree
- `crate::network::server` → `src/network/server.rs`

3. **Use modern conventions**
- Prefer `module.rs` + `module/` over `module/mod.rs`
- Cleaner, more intuitive

4. **Make submodules public explicitly**
- `pub mod` when needed outside parent
- Don't assume privacy

5. **Start simple, grow organically**
- Single file → flat structure → hierarchy
- Don't over-organize small projects

6. **Use re-exports**
- Flatten deep paths with `pub use`
- Make API ergonomic for users

7. **Keep tests separate**
- `#[cfg(test)] mod tests;` pattern
- Cleaner main files

8. **Avoid circular dependencies**
- Extract common code
- Redesign module boundaries

**Remember**: Files are for humans (organization), modules are for Rust (compilation).


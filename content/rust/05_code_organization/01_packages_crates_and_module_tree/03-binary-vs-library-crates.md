## Binary vs Library Crates

What are the key differences between binary crates and library crates in Rust?

---

**Binary Crate:**
- Compiles to an executable you can run
- Must have a `main()` function as entry point
- Default root file: `src/main.rs`
- Purpose: Create applications

**Library Crate:**
- Compiles to a library that others can use
- No `main()` function
- Default root file: `src/lib.rs`
- Purpose: Define shareable functionality


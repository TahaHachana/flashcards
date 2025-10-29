## At Most One Library Crate Rule

How many library crates can a single package contain, and why?

---

A package can contain **at most ONE library crate**.

**Why:** 
- The library crate defines the package's public API
- Having multiple libraries would create ambiguity about what the package provides
- If you need multiple libraries, create multiple packages

**However:**
- You CAN have unlimited binary crates in the same package
- You CAN split the library across multiple files (but it's still one crate)


## Module Tree Independence from Files

Why is it important to understand that the module tree is independent from file structure?

---

**Key concept**: The module tree is **logical**, file structure is **physical**.

**Implications**:

1. **Same module tree, different file layouts**:
```rust
// All in one file:
mod network { mod server {} }

// Or split across files:
// src/network.rs contains: pub mod server;
// src/network/server.rs contains server code

// Same logical tree, different physical organization
```

2. **Module relationships don't change**:
- Child modules still access parent items
- Visibility rules stay the same
- Paths remain consistent

3. **Refactoring is safe**:
- Can move code between files without changing behavior
- Only need to update `mod` declarations
- External APIs remain unchanged

**Mental model**: Module tree is the map, files are how you store the map. The map stays the same whether it's on one page or in a book.


## Mod Declaration vs Use Statement

What is the difference between `mod module_name;` and `use module_name::item;`?

---

**`mod module_name;`** - **Declares** a module
- Tells Rust the module exists
- Makes Rust look for and compile the file
- Must come before you can use items from the module

**`use module_name::item;`** - **Imports** from an already-declared module
- Brings items into scope
- Only works if module was already declared

**Example**:
```rust
// ❌ WRONG
use helper::help;  // ERROR: Can't find `helper`

// ✅ CORRECT
mod helper;        // Declare first
use helper::help;  // Then import
```

**Mental model**: `mod` makes the module exist, `use` makes items convenient to access.


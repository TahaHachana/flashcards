## What Is the Module Tree?

What is the module tree in Rust, and why does it exist?

---

The **module tree** is the hierarchical structure of modules within a crate.

**Purpose:**
- Logical organization: Group related functionality
- Control visibility: Decide what's public vs. private
- Namespace management: Avoid naming conflicts
- Code navigation: Easier to find and understand code

**Structure:**
Every crate has an implicit root module (at `src/lib.rs` or `src/main.rs`), and you define child modules to organize code hierarchically.


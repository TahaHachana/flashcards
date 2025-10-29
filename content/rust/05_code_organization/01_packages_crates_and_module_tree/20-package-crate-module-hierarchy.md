## Package, Crate, Module Hierarchy

How do packages, crates, and modules relate to each other in terms of hierarchy and purpose?

---

```
Package (Cargo concept - distribution & management)
  └── Crate(s) (Compilation unit - namespace boundary)
        └── Module Tree (Organization - visibility control)
              └── Modules (Logical grouping)
```

**Purpose of each level:**
- **Package:** Distribution, dependency management, build configuration
- **Crate:** Compilation boundary, namespace, reusable unit
- **Module Tree:** Code organization, visibility control, navigation

**Mental model:** Package = shipping box, Crates = products inside, Module tree = how each product is organized internally.


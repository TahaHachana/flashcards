## Flat vs Hierarchical Structure

When should you use a flat file structure vs a hierarchical structure?

---

**Flat structure** (all `.rs` files in `src/`):
```
src/
├── lib.rs
├── parser.rs
├── validator.rs
└── compiler.rs
```
**Good for**: Simple projects with few modules

**Hierarchical structure** (directories with submodules):
```
src/
├── lib.rs
├── database/
│   ├── mod.rs
│   ├── connection.rs
│   └── query.rs
└── api/
    ├── mod.rs
    ├── routes.rs
    └── handlers.rs
```
**Good for**: Projects with clear feature boundaries, multiple related modules

**Guideline**: Start flat, reorganize into hierarchy as project grows.


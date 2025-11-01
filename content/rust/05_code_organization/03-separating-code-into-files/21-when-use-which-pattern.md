## When to Use Which File Pattern

When should you use `module.rs` vs `module/mod.rs` vs modern `module.rs` + `module/` directory?

---

**Simple module** (no submodules):
```
src/database.rs
```
Use when: Module is self-contained with no children

**Module with submodules** (old style):
```
src/database/mod.rs
src/database/connection.rs
src/database/query.rs
```
Use when: Working with older codebases, or team preference

**Module with submodules** (modern style):
```
src/database.rs          ← Main module code
src/database/
    connection.rs        ← Submodule
    query.rs            ← Submodule
```
Use when: Rust 2018+, want cleaner structure

**Recommendation**: Use modern style for new projects (cleaner), but both are valid.


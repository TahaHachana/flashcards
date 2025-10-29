## Common Package Pattern - Single Binary

What is the most common package structure for simple applications, and when is it used?

---

```
my_app/
├── Cargo.toml
└── src/
    └── main.rs
```

**Use case:** Simple applications that don't need to share code as a library.

**Characteristics:**
- Contains only one binary crate
- All code lives in `main.rs` (or modules within it)
- Most straightforward structure for executables


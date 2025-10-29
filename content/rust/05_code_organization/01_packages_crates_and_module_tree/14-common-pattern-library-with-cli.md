## Common Package Pattern - Library with CLI

What package structure is used for libraries that also provide a CLI tool?

---

```
my_lib/
├── Cargo.toml
└── src/
    ├── lib.rs      # Core functionality
    └── main.rs     # CLI wrapper
```

**Use case:** When you want to provide both:
- A library that others can depend on (`lib.rs`)
- A command-line tool that uses the library (`main.rs`)

**Example:** A parsing library with a CLI for testing/demonstration.


## Package Structure with Multiple Crates

How do you structure a package that contains both a library crate and multiple binary crates?

---

```
my_project/
├── Cargo.toml
└── src/
    ├── lib.rs           # Library crate root
    ├── main.rs          # Primary binary crate
    └── bin/
        ├── tool1.rs     # Additional binary
        └── tool2.rs     # Additional binary
```

- Library: `src/lib.rs`
- Primary binary: `src/main.rs`
- Additional binaries: Each file in `src/bin/` becomes a separate binary crate


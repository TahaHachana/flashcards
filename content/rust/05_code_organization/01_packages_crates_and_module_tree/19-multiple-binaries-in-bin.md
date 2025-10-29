## Multiple Binary Crates in src/bin

Where do you place additional binary crates in a package, and how does Cargo handle them?

---

**Location:** `src/bin/` directory

**Structure:**
```
my_project/
└── src/
    ├── main.rs        # Primary binary
    └── bin/
        ├── tool1.rs   # Additional binary
        └── tool2.rs   # Additional binary
```

**Cargo behavior:**
- Each file in `src/bin/` automatically becomes a separate binary crate
- Each can be run with: `cargo run --bin tool1`
- Each has its own `main()` function
- All share access to the library crate (if present)


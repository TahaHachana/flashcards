## Workspace Example

Show an example of a simple workspace layout and configuration.

---

```
my_workspace/
├── Cargo.toml        # workspace root
├── core_lib/
│   └── Cargo.toml
└── cli_app/
    └── Cargo.toml
```

Root manifest:

```toml
[workspace]
members = ["core_lib", "cli_app"]
```


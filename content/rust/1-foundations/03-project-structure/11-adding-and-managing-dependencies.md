## Adding and Managing Dependencies

How can you add or update dependencies in a Cargo project?

---

Add automatically:

```bash
cargo add rand
cargo add serde --features derive
```

Update or remove:

```bash
cargo update
cargo remove rand
```

Dependencies are stored in `Cargo.toml` and cached in `~/.cargo/registry`.


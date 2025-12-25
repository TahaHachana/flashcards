## cargo doc Command

What does `cargo doc` do and what options are available?

---

Generates HTML documentation from doc comments:

```bash
# Generate documentation
cargo doc

# Generate and open in browser
cargo doc --open

# Don't document dependencies
cargo doc --no-deps

# Document private items too
cargo doc --document-private-items
```

What gets documented:
- Public items by default
- Doc comments (`///` and `//!`)
- Auto-generated trait implementations
- All dependencies (unless `--no-deps`)

Output location: `target/doc/`

Result: Professional HTML docs with:
- Searchable index
- Source code links
- Trait implementations
- Cross-references

Same format as std library docs!


## Doc Test Summary Best Practices

Summarize the key principles for effective documentation tests.

---

Key principles:

1. **Always include examples** - Most important section
2. **Keep examples simple** - One concept at a time
3. **Use hidden lines** - Hide boilerplate, show essence
4. **Verify with assert_eq!** - Not println!
5. **Test multiple scenarios** - Success, error, edge cases
6. **Use appropriate attributes**:
   - `no_run` for side effects
   - `should_panic` for errors
   - `ignore` for pseudocode
   - `compile_fail` for anti-patterns

7. **Document error cases** - Show what fails
8. **Write readable examples** - Clear variable names
9. **Test your tests** - Run `cargo test --doc`
10. **Link to related items** - Use [`Type`] syntax

Commands:
```bash
cargo test --doc      # Test docs
cargo doc --open      # View docs
```

Philosophy: Documentation IS code. Examples must compile and run correctly.


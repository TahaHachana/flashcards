## Doc Test Attributes

What attributes can you use in documentation code blocks and what do they do?

---

```rust
/// ```          - Normal (compile and run)
/// ```no_run    - Compile but don't run
/// ```ignore    - Skip test entirely
/// ```should_panic - Expect code to panic
/// ```compile_fail - Expect compilation failure
```

Examples:

```rust
/// ```no_run
/// // Compiles but doesn't run (infinite loop, network call)
/// loop { process_events(); }
/// ```

/// ```should_panic
/// divide(10, 0);  // Should panic
/// ```

/// ```ignore
/// // Pseudocode illustration
/// let result = magical_operation();
/// ```

/// ```compile_fail
/// let x: i32 = "not a number";  // Type error
/// ```
```

Use `no_run` for side effects, `should_panic` for errors, `ignore` for non-code, `compile_fail` for anti-examples.


## Failed Test Information

What key information does Rust provide when a test fails?

---

Failed test output includes:

1. **Location**: Exact file and line number
```
panicked at src/lib.rs:3:5
```

2. **Values**: What the actual values were
```
assertion `left == right` failed
  left: 4
 right: 5
```

3. **Backtrace hint**: How to get detailed stack trace
```
note: run with `RUST_BACKTRACE=1` environment variable
```

4. **Test name**: Which specific test failed
```
failures:
    test_calculation
```

This information helps quickly locate and diagnose the problem.


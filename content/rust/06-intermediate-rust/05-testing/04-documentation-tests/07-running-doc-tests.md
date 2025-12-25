## Running Documentation Tests

How do you run documentation tests and what does the output show?

---

Commands:
```bash
# Run only doc tests
cargo test --doc

# Run all tests (includes docs)
cargo test

# Filter doc tests
cargo test --doc add
```

Output:
```
   Doc-tests my_crate

running 3 tests
test src/lib.rs - add (line 5) ... ok
test src/lib.rs - multiply (line 15) ... ok
test src/lib.rs - divide (line 25) ... ok

test result: ok. 3 passed; 0 failed
```

Shows:
- File location (`src/lib.rs`)
- Function name (`add`)
- Line number where example starts (`line 5`)
- Pass/fail status

Failure shows exact panic message and location.


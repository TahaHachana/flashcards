## Quiet Output Mode

How do you get minimal test output and when would you use it?

---

Use the `-q` flag for quiet mode:

```bash
cargo test -q
```

Default output:
```
running 5 tests
test test_one ... ok
test test_two ... ok
test test_three ... ok
test test_four ... ok
test test_five ... ok

test result: ok. 5 passed; 0 failed
```

Quiet output:
```
running 5 tests
.....
test result: ok. 5 passed; 0 failed
```

Use when:
- Running many tests
- Only care about pass/fail (not names)
- Want cleaner output in scripts
- CI/CD where verbose output clutters logs

Still shows detailed output for failures.


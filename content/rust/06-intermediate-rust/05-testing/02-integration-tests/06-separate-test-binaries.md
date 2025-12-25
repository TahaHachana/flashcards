## Each File Is Separate Crate

How does Cargo treat each file in the `tests/` directory?

---

Each `.rs` file in `tests/` is compiled as a separate test binary:

```
tests/
├── api_test.rs         # Compiled as 'api_test' binary
├── integration_test.rs # Compiled as 'integration_test' binary
└── feature_test.rs     # Compiled as 'feature_test' binary
```

Output shows separate test runs:
```
running 2 tests (api_test)
test test_a ... ok
test test_b ... ok

running 1 test (integration_test)
test test_c ... ok

running 3 tests (feature_test)
test test_d ... ok
test test_e ... ok
test test_f ... ok
```

Each file independently imports and tests your library.


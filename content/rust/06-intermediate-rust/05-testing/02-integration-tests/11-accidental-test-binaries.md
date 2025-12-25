## Accidental Test Binaries Problem

What problem occurs when you create utility files directly in `tests/` directory?

---

Problem: Files become test binaries with no tests:

```
tests/
├── utils.rs         # ❌ Compiled as test binary
├── helpers.rs       # ❌ Compiled as test binary
└── actual_test.rs
```

Output shows empty test runs:
```
running 0 tests (utils)
running 0 tests (helpers)
running 1 test (actual_test)
test my_test ... ok
```

Solution: Use subdirectories:
```
tests/
├── common/
│   ├── mod.rs       # ✅ Not a test binary
│   └── helpers.rs   # ✅ Not a test binary
└── actual_test.rs   # ✅ Actual test
```

Now only `actual_test.rs` is compiled as a test binary.


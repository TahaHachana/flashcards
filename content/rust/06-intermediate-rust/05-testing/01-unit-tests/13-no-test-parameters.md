## Tests Cannot Take Parameters

Why can't test functions take parameters and how do you work around this?

---

Test functions cannot take parameters because the test runner doesn't know what values to pass.

Error:
```rust
#[test]
fn broken(input: i32) {  // Won't compile
    assert_eq!(input, 42);
}
```

Workarounds:

1. Use helper functions:
```rust
fn verify(input: i32) {
    assert_eq!(input, 42);
}

#[test]
fn test_case_1() { verify(42); }

#[test]
fn test_case_2() { verify(calculate()); }
```

2. Create separate tests:
```rust
#[test]
fn test_positive() { verify(42); }

#[test]
fn test_negative() { verify(-42); }
```


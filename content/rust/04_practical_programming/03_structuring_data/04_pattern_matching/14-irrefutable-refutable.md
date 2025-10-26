## Irrefutable vs Refutable Patterns

What is the difference between irrefutable and refutable patterns, and where can each be used?

---

**Irrefutable patterns**: Always match, can't fail
```rust
let x = 5;           // x always matches any value
let (x, y) = (1, 2); // Always destructures successfully
```

**Refutable patterns**: Might not match
```rust
Some(x)    // Might be None
Ok(value)  // Might be Err
```

**Where used**:

| Context | Requires | Example |
|---------|----------|---------|
| `let` statements | Irrefutable | `let x = 5;` ✓ |
| Function parameters | Irrefutable | `fn f(x: i32)` ✓ |
| `for` loops | Irrefutable | `for x in iter` ✓ |
| `match` arms | Refutable | `Some(x) =>` ✓ |
| `if let` | Refutable | `if let Some(x)` ✓ |
| `while let` | Refutable | `while let Some(x)` ✓ |

```rust
// ERROR: refutable pattern in let
let Some(x) = some_option;

// OK: refutable pattern in if let
if let Some(x) = some_option { }
```


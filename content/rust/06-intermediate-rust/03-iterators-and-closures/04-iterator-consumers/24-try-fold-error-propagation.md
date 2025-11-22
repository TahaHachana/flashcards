## Try Fold Error Propagation

What does `.try_fold()` do? How does it differ from regular `.fold()`?

---

`.try_fold()` is like `.fold()` but can short-circuit on error, returning `Result`.

**Signature:**
```rust
fn try_fold<B, F, R>(&mut self, init: B, f: F) -> R
where
    F: FnMut(B, Self::Item) -> R,
    R: Try<Output = B>
```

**Regular fold - no early exit:**
```rust
let sum = numbers.iter()
    .fold(0, |acc, &x| {
        acc + x
    });
// Must process all elements
```

**Try fold - can fail and stop:**
```rust
let result: Result<i32, Error> = numbers.iter()
    .try_fold(0, |acc, &x| {
        if x < 0 {
            Err(Error::NegativeNumber)
        } else {
            Ok(acc + x)
        }
    });
// Stops at first error
```

**Validating while accumulating:**
```rust
let validated_sum: Result<i32, String> = inputs.iter()
    .try_fold(0, |acc, input| {
        let value = input.parse::<i32>()
            .map_err(|_| format!("Invalid: {}", input))?;
        Ok(acc + value)
    });
```

**Building with fallible operations:**
```rust
let result: Result<Vec<Item>, Error> = data.iter()
    .try_fold(Vec::new(), |mut acc, elem| {
        let processed = elem.try_process()?;
        acc.push(processed);
        Ok(acc)
    });
```

**Key differences from fold:**

| Aspect | fold | try_fold |
|--------|------|----------|
| Return type | `B` | `Result<B, E>` or `Option<B>` |
| Early exit | No | Yes (on Err/None) |
| Error handling | Can't propagate | Can propagate with `?` |

**Works with Option too:**
```rust
let first_negative: Option<i32> = numbers.iter()
    .try_fold((), |_, &x| {
        if x < 0 {
            None  // Stop and return None
        } else {
            Some(())  // Continue
        }
    })
    .map(|_| None)
    .unwrap_or_else(|| Some(/* found */));
```

**Use when:**
- Accumulation can fail
- Need error propagation
- Want early termination on error
- Building fallible structures

More powerful than fold when dealing with errors.


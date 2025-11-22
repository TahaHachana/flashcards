## Collect Error Handling Pattern

Show the pattern for collecting Results with error handling, including both "stop at first error" and "collect all errors" approaches.

---

Different patterns for handling errors when collecting Results.

**Pattern 1: Stop at first error**
```rust
// Returns Result<Vec<T>, E>
let results: Result<Vec<i32>, _> = inputs.iter()
    .map(|input| process_with_error(input))
    .collect();

match results {
    Ok(values) => println!("All succeeded: {:?}", values),
    Err(e) => println!("Failed at first error: {}", e),
}
```

**Pattern 2: Separate successes and failures**
```rust
let (successes, failures): (Vec<_>, Vec<_>) = inputs.iter()
    .map(|input| process_with_error(input))
    .partition(Result::is_ok);

let successes: Vec<T> = successes.into_iter()
    .map(Result::unwrap)
    .collect();

let errors: Vec<E> = failures.into_iter()
    .map(Result::unwrap_err)
    .collect();
```

**Pattern 3: Filter to only successes**
```rust
let successes: Vec<T> = inputs.iter()
    .map(|input| process_with_error(input))
    .filter_map(Result::ok)
    .collect();
// Discards all errors
```

**Pattern 4: Collect all errors if any**
```rust
let results: Vec<Result<T, E>> = inputs.iter()
    .map(|input| process_with_error(input))
    .collect();

let has_errors = results.iter().any(Result::is_err);
if has_errors {
    let errors: Vec<_> = results.iter()
        .filter_map(|r| r.as_ref().err())
        .collect();
    return Err(MultipleErrors(errors));
}

let values: Vec<T> = results.into_iter()
    .map(Result::unwrap)
    .collect();
```

**Pattern 5: Accumulate errors with fold**
```rust
let (values, errors): (Vec<T>, Vec<E>) = inputs.iter()
    .map(|input| process_with_error(input))
    .fold((Vec::new(), Vec::new()), |(mut ok, mut err), result| {
        match result {
            Ok(v) => ok.push(v),
            Err(e) => err.push(e),
        }
        (ok, err)
    });

if !errors.is_empty() {
    // Handle errors
}
```

**Key insight:** `.collect()` on `Result` automatically implements "stop at first error" semantics. For other behaviors, use `partition`, `filter_map`, or `fold`.


## Box<dyn Error> Pattern

Why is `Box<dyn Error>` commonly used in error handling?

---

`Box<dyn Error>` allows returning different error types from the same function:

```rust
use std::error::Error;

#[derive(Debug)]
struct ErrorOne;
impl Error for ErrorOne { }
impl Display for ErrorOne { /* ... */ }

#[derive(Debug)]
struct ErrorTwo;
impl Error for ErrorTwo { }
impl Display for ErrorTwo { /* ... */ }

fn do_something(flag: bool) -> Result<String, Box<dyn Error>> {
    if flag {
        Err(Box::new(ErrorOne))  // Different type
    } else {
        Err(Box::new(ErrorTwo))  // Different type
    }
}
```

All errors implement `Error`, so they can all fit in `Box<dyn Error>`.


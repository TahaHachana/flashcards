## Handling Name Conflicts with Aliases

How do you handle naming conflicts when two imported items have the same name?

---

**Use aliases** with `as` keyword:

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn format_output() -> Result {
    // Returns fmt::Result
    Ok(())
}

fn read_file() -> IoResult<String> {
    // Returns io::Result
    Ok(String::new())
}
```

**Alternative - use parent modules**:
```rust
use std::fmt;
use std::io;

fn format_output() -> fmt::Result { /* ... */ }
fn read_file() -> io::Result<String> { /* ... */ }
```

**When to use**:
- Two items have same name
- Want to clarify which you're using
- Type name is too generic (like `Result` or `Error`)

**Pattern**: Keep commonly used one without alias, alias the other.


## if let Expression

When should you use if let instead of match, and what is its syntax?

---

**Use if let** when you only care about one pattern and want to ignore the rest.

**Syntax**: `if let PATTERN = VALUE`

```rust
// With match (verbose)
match some_value {
    Some(3) => println!("three"),
    _ => {},  // Must handle other cases
}

// With if let (concise)
if let Some(3) = some_value {
    println!("three");
}

// With else
if let Some(value) = some_value {
    println!("Got: {}", value);
} else {
    println!("Got nothing");
}
```

**Guideline**: 
- Use `match` for multiple patterns
- Use `if let` for single pattern (more readable)
- Both are expressions that can return values


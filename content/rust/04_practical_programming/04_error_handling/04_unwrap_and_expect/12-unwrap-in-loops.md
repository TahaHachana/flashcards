## Unwrap In Loops

What's the problem with using `unwrap()` inside loops and how do you handle it better?

---

**Bad - first error stops everything:**
```rust
fn process_all(items: Vec<&str>) -> Vec<i32> {
    items.iter()
        .map(|s| s.parse::<i32>().unwrap())  // Panics on first bad item
        .collect()
}
```

**Good - skip bad items:**
```rust
fn process_all(items: Vec<&str>) -> Vec<i32> {
    items.iter()
        .filter_map(|s| match s.parse::<i32>() {
            Ok(n) => Some(n),
            Err(e) => {
                eprintln!("Warning: Can't parse '{}': {}", s, e);
                None
            }
        })
        .collect()
}
```

**Or fail properly:**
```rust
fn process_all_strict(items: Vec<&str>) -> Result<Vec<i32>, String> {
    items.iter()
        .map(|s| s.parse::<i32>().map_err(|e| e.to_string()))
        .collect()
}
```


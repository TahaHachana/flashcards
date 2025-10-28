## Question Mark In Iterators

How do you use `?` effectively with iterators and `collect()`?

---

`collect()` can automatically propagate errors from an iterator of Results:

```rust
fn parse_all(strings: Vec<&str>) -> Result<Vec<i32>, String> {
    strings.iter()
        .map(|s| s.parse::<i32>().map_err(|e| e.to_string()))
        .collect()  // Returns Err at first error
}
```

For more control, use `try_fold`:

```rust
fn sum_parsed(strings: Vec<&str>) -> Result<i32, String> {
    strings.iter()
        .try_fold(0, |acc, s| {
            let num = s.parse::<i32>()
                .map_err(|e| e.to_string())?;
            Ok(acc + num)
        })
}
```


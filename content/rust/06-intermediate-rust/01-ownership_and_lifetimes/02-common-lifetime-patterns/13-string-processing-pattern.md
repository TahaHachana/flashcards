## String Processing Pattern

What lifetime pattern is used when extracting a substring from borrowed text?

```rust
fn get_line<'a>(text: &'a str, line_num: usize) -> Option<&'a str> {
    text.lines().nth(line_num)
}
```

---

This uses Pattern 1 (Input-Output Flow, Single Source). The output substring is a slice of the input text, so it has the same lifetime `'a` as the input. The line number is a value type (usize), not a reference, so it doesn't affect lifetimes.


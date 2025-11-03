## Pattern Single Input Single Output

Which elision rule applies to this pattern, and why does it work?

```rust
fn first_word(s: &str) -> &str {
    s.split_whitespace().next().unwrap_or("")
}
```

---

Rule 2 applies. There's exactly one input reference (`s`), so that lifetime is assigned to the output. The expanded version is:
```rust
fn first_word<'a>(s: &'a str) -> &'a str
```
This works because with only one input reference, any returned reference must come from it.


## Finding Maximum Pattern

What lifetime pattern does this collection operation use, and why?

```rust
fn find_max<'a>(values: &'a [i32]) -> Option<&'a i32> {
    values.iter().max()
}
```

---

Pattern 1 (Input-Output Flow, Single Source). The maximum value is an element within the slice, so the returned reference has the same lifetime `'a` as the input slice. The `Option` accounts for the case of an empty slice. This is the same pattern used for any operation that extracts or filters elements from a collection.


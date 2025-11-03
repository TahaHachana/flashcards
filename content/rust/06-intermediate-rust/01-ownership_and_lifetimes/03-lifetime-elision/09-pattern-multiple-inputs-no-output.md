## Pattern Multiple Inputs No Output

Which elision rule applies when a function has multiple reference inputs but doesn't return references?

```rust
fn compare(x: &str, y: &str) -> bool {
    x.len() > y.len()
}
```

---

Rule 1 applies (each input gets its own lifetime), but since there are no output references, lifetime relationships don't matter. Expanded:
```rust
fn compare<'a, 'b>(x: &'a str, y: &'b str) -> bool
```
This works because without output references, the input lifetimes don't need to be related.


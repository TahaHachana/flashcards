## Gotcha Over-Constraining with Single Lifetime

When might using a single lifetime parameter be too restrictive, and what's the solution?

---

If fields can have independent lifetimes but you force them to share one:
```rust
struct Document<'a> {
    title: &'a str,
    body: &'a str,
}
```
Both must live equally long. If they can have different lifetimes:
```rust
struct Document<'a, 'b> {
    title: &'a str,
    body: &'b str,
}
```
However, only use multiple lifetimes if you actually need them—single lifetime is simpler.


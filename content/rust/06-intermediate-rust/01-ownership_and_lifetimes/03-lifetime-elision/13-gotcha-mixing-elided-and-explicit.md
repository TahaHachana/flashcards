## Gotcha Mixing Elided and Explicit

What's the problem with mixing elided and explicit lifetimes in a signature?

```rust
fn example<'a>(x: &'a str, y: &str) -> &'a str {
    x
}
```

---

Mixing elision and explicit lifetimes in a signature is confusing and often indicates a design issue. Be consistent—either use elision throughout or use explicit lifetimes throughout. This signature should be either:
```rust
// All explicit
fn example<'a, 'b>(x: &'a str, y: &'b str) -> &'a str
// Or let both elide if possible
```


## Lifetime Subtyping Syntax

What does the lifetime bound `'b: 'a` mean in this struct?
```rust
struct Nested<'a, 'b: 'a> {
    long: &'a str,
    short: &'b str,
}
```

---

`'b: 'a` means "`'b` outlives `'a`" or "`'b` lives at least as long as `'a`". This expresses a precise relationship between the two lifetimes. This syntax is rarely needed in practice but can be useful for expressing complex lifetime constraints when you have multiple lifetime parameters with hierarchical relationships.


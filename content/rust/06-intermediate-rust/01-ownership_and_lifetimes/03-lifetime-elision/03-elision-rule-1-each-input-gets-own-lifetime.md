## Elision Rule 1 Each Input Gets Own Lifetime

What is Elision Rule 1, and what does it do?

---

Rule 1: Each elided lifetime in function parameters gets its own distinct lifetime parameter.

Example:
```rust
// What you write
fn foo(x: &i32, y: &i32) -> i32

// What the compiler sees
fn foo<'a, 'b>(x: &'a i32, y: &'b i32) -> i32
```

This applies to all reference parameters without explicit lifetimes. The rule exists because when a function doesn't return references, input lifetimes don't need to be related.


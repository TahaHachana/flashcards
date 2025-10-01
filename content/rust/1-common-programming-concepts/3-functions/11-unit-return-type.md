## Unit Return Type

What return type do functions without `->` in Rust have?

---

They implicitly return the unit type `()`.

```rust
fn do_nothing() {
    // implicitly returns ()
}
```


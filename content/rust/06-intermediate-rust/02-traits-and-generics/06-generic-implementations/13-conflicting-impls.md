## Conflicting Implementations

What causes conflicting implementations, and how do you avoid them?

---

Conflict occurs when multiple impl blocks could provide the same method:

```rust
impl<T> Container<T> {
    fn process(&self) {
        println!("Generic");
    }
}

// ❌ ERROR: Conflicting implementation
impl<T: Display> Container<T> {
    fn process(&self) {  // Same method name!
        println!("Display");
    }
}
```

**Solutions**:
1. Use different method names:
```rust
impl<T: Display> Container<T> {
    fn process_display(&self) { /* ... */ }
}
```

2. Ensure bounds don't overlap (not always possible)


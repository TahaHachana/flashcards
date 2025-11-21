## Premature Optimization Mistake

What is the most common mistake developers make when choosing between static and dynamic dispatch?

---

**Premature optimization** - assuming dynamic dispatch is "too slow" without measuring:

```rust
// ❌ Bad: Over-optimizing rarely-called code
fn log_event<T: Display>(event: T) {
    // Called once per minute, but using generics "for performance"
    println!("{}", event);
}

// ✅ Better: Use trait object for simplicity
fn log_event(event: &dyn Display) {
    // Simpler API, smaller binary
    // 2ns overhead per minute = completely negligible
    println!("{}", event);
}
```

**Rule**: Start with trait objects for simplicity. Only switch to generics if profiling shows a bottleneck.

Dynamic dispatch overhead (~2-5ns) only matters in hot paths called millions of times.


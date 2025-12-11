## Arc Clone Performance Optimization

What are three ways to optimize Arc clone performance?

---

**1. Clone once, reuse multiple times:**
```rust
// ❌ Bad: Clone in every iteration
for i in 0..1000 {
    let data_clone = Arc::clone(&data);
    use_data(&data_clone);
}

// ✅ Good: Clone once, reuse
let data_clone = Arc::clone(&data);
for i in 0..1000 {
    use_data(&data_clone);
}
```

**2. Pass Arc by reference when possible:**
```rust
// ❌ Clone to pass to function
fn process(data: Arc<Data>) { }
process(Arc::clone(&data));

// ✅ Better: pass reference, no clone
fn process(data: &Arc<Data>) { }
process(&data);
```

**3. Minimize Arc scope:**
```rust
// ❌ Arc lives longer than needed
let data = Arc::new(expensive_data);
// ... lots of code ...
use_data(&data);

// ✅ Create Arc close to where it's needed
// ... lots of code ...
let data = Arc::new(expensive_data);
use_data(&data);
```

**Benchmark difference:**
```rust
// Clone in loop: ~1000ms
// Clone once: ~10ms
// 100x faster!
```

**Key principle:** Atomic operations are fast but not free. Minimize unnecessary clones.


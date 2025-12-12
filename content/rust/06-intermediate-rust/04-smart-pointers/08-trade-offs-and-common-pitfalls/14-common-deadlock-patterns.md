## Common Deadlock Patterns

Describe three common deadlock patterns and their solutions.

---

**Pattern 1: Lock ordering**
```rust
// ❌ Deadlock: inconsistent order
Thread A: lock(1) → lock(2)
Thread B: lock(2) → lock(1)

// ✅ Fix: consistent order
Thread A: lock(1) → lock(2)
Thread B: lock(1) → lock(2)
```

**Pattern 2: Nested locks**
```rust
// ❌ Deadlock: hidden nesting
fn process(m1: &Mutex<i32>, m2: &Mutex<i32>) {
    let g1 = m1.lock().unwrap();
    // Might call function that locks m2
    helper(m2);  // Could deadlock
}

// ✅ Fix: avoid nesting or use consistent order
fn process(m1: &Mutex<i32>, m2: &Mutex<i32>) {
    let g1 = m1.lock().unwrap();
    drop(g1);  // Release first
    helper(m2);  // Then lock second
}
```

**Pattern 3: Lock held across await (async)**
```rust
// ❌ Deadlock: guard held across await
async fn process(mutex: Arc<Mutex<Data>>) {
    let guard = mutex.lock().unwrap();
    some_async_operation().await;  // ⚠️ Guard held
}

// ✅ Fix: drop guard before await
async fn process(mutex: Arc<Mutex<Data>>) {
    let data = {
        let guard = mutex.lock().unwrap();
        guard.clone()
    };  // Guard dropped
    some_async_operation().await;  // Safe
}
```

**Prevention summary:**
1. Consistent lock ordering
2. Minimize lock duration  
3. Avoid nested locks
4. Never hold locks across await points


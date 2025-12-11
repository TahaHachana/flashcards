## Arc vs Rc Comparison

Compare `Arc` and `Rc` across key features. When should you use each?

---

| Feature | Rc | Arc |
|---------|-----|-----|
| **Thread-safe** | No | Yes |
| **Counting** | Non-atomic | Atomic |
| **Performance** | Faster | Slightly slower |
| **Send** | No | Yes |
| **Sync** | No | Yes |
| **Use case** | Single-threaded | Multi-threaded |

**Simple rule:**
- One thread? → Use `Rc` (faster)
- Multiple threads? → Use `Arc` (thread-safe)

**Example:**
```rust
// Single-threaded: use Rc
let rc = Rc::new(data);

// Multi-threaded: use Arc
let arc = Arc::new(data);
thread::spawn(move || {
    // Use arc
});
```

**Performance difference:** Arc is ~50% slower due to atomic operations, but still very fast in absolute terms.


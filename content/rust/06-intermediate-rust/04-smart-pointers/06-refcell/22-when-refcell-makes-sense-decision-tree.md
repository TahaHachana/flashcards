## When RefCell Makes Sense Decision Tree

Create a decision tree for determining when to use `RefCell`.

---

```
Need to mutate data?
  │
  ├─ No → Don't use RefCell
  │
  └─ Yes → Have &mut access?
      │
      ├─ Yes → Use regular &mut (prefer this)
      │        Don't need RefCell
      │
      └─ No → Why not?
          │
          ├─ API requires &self → RefCell candidate ✓
          │   │
          │   ├─ Single-threaded? → Use RefCell
          │   └─ Multi-threaded? → Use Mutex
          │
          ├─ Multiple owners need mutation
          │   │
          │   ├─ Single-threaded? → Rc<RefCell<T>>
          │   └─ Multi-threaded? → Arc<Mutex<T>>
          │
          └─ Building mock/cache/graph? → RefCell candidate ✓
```

**Quick checks:**
```rust
// ✅ Good for RefCell
trait Component {
    fn update(&self);  // API forces &self
}

// ❌ Bad - just use mut
fn process(data: &mut Vec<i32>) {
    // Have &mut, don't need RefCell
}

// ✅ Good for RefCell
struct Cache {
    data: RefCell<HashMap<K, V>>,  // Interior mutability
}
```

**Rule of thumb:** If you can use regular `&mut`, do that. Use RefCell only when the API or architecture makes it necessary.


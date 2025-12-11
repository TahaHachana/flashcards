## Compile-Time vs Runtime Safety Trade-off

Compare compile-time vs runtime borrow checking. What are the trade-offs?

---

**Compile-time checking (regular Rust):**
```rust
let mut x = 5;
let r1 = &x;
// let r2 = &mut x;  // ❌ Won't compile
```

**Pros:**
- Catch bugs at compile time (earlier = better)
- Zero runtime cost
- Can't forget to check
- Guaranteed safe

**Cons:**
- Less flexible
- Can't express some patterns
- More restrictive

**Runtime checking (RefCell):**
```rust
let x = RefCell::new(5);
let r1 = x.borrow();
// let r2 = x.borrow_mut();  // ⚠️ Will panic
```

**Pros:**
- More flexible
- Can express patterns impossible otherwise
- Works with APIs requiring `&self`

**Cons:**
- Can panic at runtime (bugs reach production)
- Small runtime cost
- Must manually ensure correctness
- Need tests to catch violations

**Trade-off decision matrix:**
```
Can satisfy borrows at compile time?
  ├─ Yes → Use regular mut (safer, faster)
  └─ No → Consider RefCell
      ├─ Single-threaded? → RefCell
      └─ Multi-threaded? → Mutex
```

**Rule:** Prefer compile-time safety (regular mut) when possible. Use RefCell when architecture demands runtime flexibility.


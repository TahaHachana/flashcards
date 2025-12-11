## Understanding Atomic Operations

What are atomic operations, and how do they make `Arc` thread-safe? Show the difference between atomic and non-atomic operations.

---

**Atomic** means "indivisible" - an operation that either completes fully or doesn't happen at all. No thread can see the operation "in progress."

**Non-atomic operation (Rc):**
```
Thread 1: Read count (5)
Thread 2: Read count (5)    ← Both see 5 at same time!
Thread 1: Write count (6)
Thread 2: Write count (6)   ← Lost Thread 1's increment!
Result: Count is 6, should be 7 ❌
```

**Atomic operation (Arc):**
```
Thread 1: Atomic increment (5 → 6)  ← Complete operation
Thread 2: Atomic increment (6 → 7)  ← Complete operation
Result: Count is 7 ✓
```

**How Arc uses atomics:**
- Counter updates are indivisible
- Other threads must wait for operation to complete
- No race conditions possible
- Always produces correct count

**Example race condition without atomics:**
```rust
// Thread 1 and 2 both do: x += 1
// Expected final value: 12
// Actual: 11-12 (unpredictable)
```

With Arc's atomic operations, result is always predictable and correct.


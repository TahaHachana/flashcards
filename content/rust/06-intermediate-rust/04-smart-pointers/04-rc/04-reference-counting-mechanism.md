## Reference Counting Mechanism

Explain how reference counting works in `Rc<T>`. Show the count changing through creation, clones, and drops.

---

`Rc` maintains a count of how many `Rc` pointers exist to the data:

```rust
use std::rc::Rc;

let data = Rc::new(String::from("hello"));
println!("Count: {}", Rc::strong_count(&data));  // 1

let data2 = Rc::clone(&data);
println!("Count: {}", Rc::strong_count(&data));  // 2

let data3 = Rc::clone(&data);
println!("Count: {}", Rc::strong_count(&data));  // 3

drop(data2);
println!("Count: {}", Rc::strong_count(&data));  // 2

drop(data3);
println!("Count: {}", Rc::strong_count(&data));  // 1
// data dropped, count = 0, memory freed
```

**The lifecycle:**
1. **Create**: `Rc::new()` → count = 1
2. **Clone**: `Rc::clone()` → count increments
3. **Drop**: Each drop → count decrements
4. **Cleanup**: Count reaches 0 → data freed automatically

**Memory layout:**
```
Heap:
┌──────────────────┐
│ Strong Count: 3  │
│ Weak Count: 0    │
│ Data: "hello"    │
└──────────────────┘
   ↑   ↑   ↑
  rc1 rc2 rc3
```


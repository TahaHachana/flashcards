## Rc<RefCell<T>> Pattern

What is `Rc<RefCell<T>>`, what does each layer provide, and when should you use it?

---

**What it provides:**
```
Rc<RefCell<T>>
│
├─ Rc: Multiple owners can share the same data
│
└─ RefCell: Data can be mutated through immutable references
```

**Capabilities:**
- ✅ Multiple owners (reference counting)
- ✅ Interior mutability (runtime borrow checking)
- ✅ Single-threaded (no atomic overhead)
- ❌ Not thread-safe

**When to use:**
1. Multiple parts of code need to own the data
2. Data needs to be mutable
3. Code is single-threaded
4. Building complex data structures (graphs, trees)

**Example:**
```rust
use std::rc::Rc;
use std::cell::RefCell;

let data = Rc::new(RefCell::new(vec![1, 2, 3]));

let data1 = Rc::clone(&data);
let data2 = Rc::clone(&data);

// Both can mutate
data1.borrow_mut().push(4);
data2.borrow_mut().push(5);

println!("{:?}", data.borrow());  // [1, 2, 3, 4, 5]
```

**Common use cases:** UI component trees, game entity graphs, single-threaded event systems


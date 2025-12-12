## Common RefCell Panic Scenarios

Describe three common scenarios that cause RefCell panics and how to avoid each.

---

**Scenario 1: Forgetting guards are held**
```rust
let cell = RefCell::new(vec![]);

// ❌ Panic
let borrow = cell.borrow();
// ... lots of code ...
cell.borrow_mut();  // Panic! borrow still alive

// ✅ Fix: explicit scope
{
    let borrow = cell.borrow();
    // Use borrow
}  // Dropped
cell.borrow_mut();  // Safe
```

**Scenario 2: Double borrow in expression**
```rust
// ❌ Panic: both borrows active simultaneously
cell.borrow_mut().push(*cell.borrow().first().unwrap());

// ✅ Fix: separate borrows
let first = *cell.borrow().first().unwrap();
cell.borrow_mut().push(first);
```

**Scenario 3: Recursive function calls**
```rust
struct Data {
    value: RefCell<i32>,
}

impl Data {
    fn process(&self) {
        let mut val = self.value.borrow_mut();
        *val += 1;
        self.helper();  // ⚠️ Might try to borrow again
    }
    
    fn helper(&self) {
        let val = self.value.borrow();  // Panic if borrow_mut active
        println!("{}", *val);
    }
}

// ✅ Fix: drop guard before calling helper
fn process(&self) {
    {
        let mut val = self.value.borrow_mut();
        *val += 1;
    }  // Dropped
    self.helper();  // Safe
}
```

**Prevention:** Keep borrow lifetimes as short as possible.


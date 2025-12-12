## When Not to Use Smart Pointers

Give three examples where using smart pointers is unnecessary and show the simpler alternative.

---

**1. Single owner doesn't need Arc:**
```rust
// ❌ Unnecessary
let data = Arc::new(vec![]);
// Only used in one thread

// ✅ Simple ownership
let data = vec![];
```

**2. Can use &mut instead of RefCell:**
```rust
// ❌ Overcomplicating
struct Container {
    data: RefCell<Vec<i32>>,
}

fn process(c: &Container) {
    c.data.borrow_mut().push(1);
}

// ✅ Simple mut
struct Container {
    data: Vec<i32>,
}

fn process(c: &mut Container) {
    c.data.push(1);
}
```

**3. Cloning Arc when borrowing works:**
```rust
// ❌ Unnecessary clone
fn helper(data: Arc<Data>) { }
helper(Arc::clone(&data));

// ✅ Borrow when possible
fn helper(data: &Data) { }
helper(&data);
```

**Principle:** Start with simplest option:
1. Stack allocation (default)
2. Regular ownership
3. Borrowing (&T, &mut T)
4. Smart pointers (only when needed)

Add complexity only when requirements demand it.


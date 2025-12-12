## Overusing Smart Pointers

Show three examples of unnecessarily using smart pointers and the simpler alternative.

---

**Example 1: Single owner using Arc**
```rust
// ❌ Overuse: Arc for single thread
fn process(data: Arc<Vec<i32>>) {
    // Only used here, never shared
}

// ✅ Simple ownership
fn process(data: Vec<i32>) {
    // Direct ownership
}
```

**Example 2: Unnecessary RefCell**
```rust
// ❌ Overuse: RefCell when &mut works
struct Container {
    data: RefCell<Vec<i32>>,
}

fn update(c: &Container) {
    c.data.borrow_mut().push(1);
}

// ✅ Simple mut
struct Container {
    data: Vec<i32>,
}

fn update(c: &mut Container) {
    c.data.push(1);
}
```

**Example 3: Cloning Arc when borrowing works**
```rust
// ❌ Unnecessary clone
fn helper(data: Arc<Data>) {
    // data used here
}
helper(Arc::clone(&data));

// ✅ Borrow when possible
fn helper(data: &Data) {
    // data used here
}
helper(&data);
```

**Signs of overuse:**
- Single owner using `Arc`
- Can use `&mut` but using `RefCell`
- Cloning smart pointers when borrowing works
- No threading but using `Arc`/`Mutex`

**Principle:** Start simple:
1. Stack allocation
2. Regular ownership
3. Borrowing
4. Smart pointers (only when needed)


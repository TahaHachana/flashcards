## When Each Smart Pointer is Appropriate

Create a decision guide: given different scenarios, which smart pointer should you use?

---

**Use `Box<T>` when:**
- You have a large value and want to avoid stack overflow
- You need a recursive/self-referential type
- You want ownership but heap allocation
- You need a trait object with single ownership

**Use `Rc<T>` when:**
- Multiple parts of code need to read the same data
- Single-threaded context only
- You don't need to mutate (or use with `RefCell` for mutation)
- Example: graph nodes, cached data, shared configs

**Use `Arc<T>` when:**
- Same as `Rc<T>` but in multi-threaded context
- Sharing data across threads
- Often paired with `Mutex`: `Arc<Mutex<T>>`

**Use `RefCell<T>` when:**
- You need interior mutability (mutate through `&`)
- Borrow rules are too restrictive at compile time
- You're confident runtime checks won't panic
- Often paired with `Rc`: `Rc<RefCell<T>>`

**Quick decision tree:**
1. Single owner? → `Box<T>`
2. Multiple owners, single thread? → `Rc<T>`
3. Multiple owners, multiple threads? → `Arc<T>`
4. Need mutation through `&`? → `RefCell<T>`


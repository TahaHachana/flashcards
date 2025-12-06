## Overview of Rust's Smart Pointer Family

List the main smart pointers in Rust's standard library with their primary purposes.

---

**`Box<T>`**: Heap allocation and indirection
- Single owner, data on heap

**`Rc<T>`**: Reference counting for single-threaded shared ownership
- Multiple owners, single-threaded only

**`Arc<T>`**: Atomic reference counting for multi-threaded shared ownership
- Multiple owners, thread-safe

**`RefCell<T>`**: Interior mutability with runtime borrow checking
- Single owner, allows mutation through immutable references

**`Cow<T>`**: Clone-on-write
- Delays cloning until mutation is needed

**`Mutex<T>` / `RwLock<T>`**: Thread-safe interior mutability
- For concurrent access to shared mutable data


## Box Doesn't Implement Copy

Why doesn't `Box<T>` implement `Copy`, and what do you use instead?

---

`Box<T>` doesn't implement `Copy` because copying a `Box` would mean duplicating the heap allocation, which is expensive and could be unexpected.

**Example showing the issue:**
```rust
fn just_takes<T>(item: T) {}

let my_number = 1;
just_takes(my_number);
just_takes(my_number);  // ✅ Works - i32 is Copy

let my_box = Box::new(1);
just_takes(my_box.clone());  // Need explicit clone
just_takes(my_box);          // ✅ Works - first was cloned
```

**Solution:** Use `.clone()` explicitly when you need a copy. This:
- Makes the cost visible (explicit heap allocation)
- Prevents accidental expensive operations
- Forces you to think about whether you really need a copy

`Box` implements `Clone`, not `Copy`, requiring explicit duplication.


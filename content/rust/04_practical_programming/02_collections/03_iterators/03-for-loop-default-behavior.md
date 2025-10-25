## For Loop Default Behavior

What does `for item in vec` do to ownership? How do you prevent this?

---

`for item in vec` calls `.into_iter()`, consuming the collection.

**Prevent by borrowing**:
```rust
for item in &vec { }      // Same as vec.iter()
for item in &mut vec { }  // Same as vec.iter_mut()
```
Use `&vec` to keep the collection usable afterward.


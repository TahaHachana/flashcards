## For Each Consumer

What does `.for_each()` do and when should you use it instead of `.collect()`?

---

`.for_each()` executes a closure on each item without collecting results. Use for side effects:
```rust
vec.iter().for_each(|x| println!("{}", x));

// Equivalent to:
for x in vec.iter() {
    println!("{}", x);
}
```
Use when you don't need a new collection, just want to do something with each item.


## Peekable Iterator

What does `.peekable()` enable and how do you use it?

---

Allows looking at next item without consuming it:
```rust
let mut iter = vec![1, 2, 3].into_iter().peekable();

if let Some(&next) = iter.peek() {
    println!("Next is: {}", next);  // 1
}
let first = iter.next();  // Still Some(1)
```
`.peek()` returns `Option<&T>` without advancing iterator.


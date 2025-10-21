## Automatic Drop for String

What happens when a String goes out of scope?

---

Compiler calls drop(), String's drop implementation frees the heap allocation, then the stack portion is removed.

```rust
{
    let s = String::from("hello");
}  // Drop frees heap memory automatically
```


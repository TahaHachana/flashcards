## Overly Restrictive Bounds

What's the problem with adding too many trait bounds, and how do you avoid it?

---

Overly restrictive bounds limit which types can use your function unnecessarily:

```rust
// ❌ Too restrictive - only needs T to exist!
fn get_first<T: Debug + Clone + Display>(vec: Vec<T>) -> Option<T> {
    vec.into_iter().next()
}

// ✅ Better - no unnecessary bounds
fn get_first<T>(vec: Vec<T>) -> Option<T> {
    vec.into_iter().next()
}
```

**Rule**: Only add trait bounds for operations you actually perform in the function. Don't add "just in case" bounds.


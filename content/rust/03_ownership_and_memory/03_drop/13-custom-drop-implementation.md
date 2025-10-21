## Custom Drop Implementation

How do you implement custom cleanup for a type?

---

Implement the Drop trait with a drop method defining cleanup behavior.

```rust
impl Drop for FileHandler {
    fn drop(&mut self) {
        println!("Closing file");
        // Cleanup code here
    }
}
```


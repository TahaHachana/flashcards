## Consuming Ownership Pattern

What does it mean for a function to "consume" ownership?

---

The function takes ownership and doesn't return it. The value is dropped when the function ends.

```rust
fn consume(s: String) {
    // Use s
}  // s dropped here
let data = String::from("hello");
consume(data);  // data is gone
```


## First and Last Element Access

What are the two ways to safely access the first element of a vector?

---

```rust
let vec = vec![1, 2, 3];

// Method 1: Using .get()
if let Some(&first) = vec.get(0) {
    println!("{}", first);
}

// Method 2: Using .first()
if let Some(&first) = vec.first() {
    println!("{}", first);
}
```
Both return `Option<&T>`.


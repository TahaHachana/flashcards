## Array Basics

How do you declare arrays in Rust, and what are their constraints?

---

* Arrays have fixed length.
* All elements must be the same type.
* Stored on the stack (faster than `Vec`).

Example:

```rust
let a = [1, 2, 3, 4, 5];
let months = ["Jan", "Feb", "Mar"];
let a: [i32; 5] = [1, 2, 3, 4, 5];
let a = [3; 5]; // [3, 3, 3, 3, 3]
```


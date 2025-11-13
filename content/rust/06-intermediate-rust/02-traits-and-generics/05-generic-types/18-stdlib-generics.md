## Generics and Standard Library

How does understanding generics help you use standard library types?

---

Most standard library types are generic. Understanding generics helps you:

```rust
// Vec is generic over T
let numbers: Vec<i32> = Vec::new();
let words: Vec<String> = Vec::new();

// HashMap is generic over K and V
let map: HashMap<String, i32> = HashMap::new();

// Option is generic over T
let some_number: Option<i32> = Some(5);
let some_text: Option<String> = Some(String::from("hi"));

// Result is generic over T and E
let result: Result<i32, String> = Ok(42);
```

When you see `Vec<T>`, `Option<T>`, or `Result<T, E>`, you know they're generic types that work with any type you specify.


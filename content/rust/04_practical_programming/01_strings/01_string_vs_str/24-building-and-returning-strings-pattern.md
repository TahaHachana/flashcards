## Building and Returning Strings Pattern

Why should functions that create strings return String rather than &str?

---

Functions return String to transfer ownership of newly created data:
```rust
fn create_message(name: &str, age: u32) -> String {
    format!("{} is {} years old", name, age)
}

let msg = create_message("Alice", 30);
// msg owns the String
```
Returning &str would require the string to outlive the function, which is impossible for locally created data. String transfers ownership to the caller.


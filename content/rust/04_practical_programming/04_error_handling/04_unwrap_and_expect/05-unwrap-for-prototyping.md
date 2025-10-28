## Unwrap For Prototyping

When is it acceptable to use `unwrap()` in prototype or example code?

---

During prototyping or in example code to focus on the main concept:

```rust
// Example code - focus on JSON parsing, not error handling
fn example_json_parsing() {
    let json = r#"{"name": "Alice", "age": 30}"#;
    let value: serde_json::Value = serde_json::from_str(json).unwrap();
    println!("Name: {}", value["name"]);
}
```

**Important caveats:**
- Add a TODO comment to replace it before production
- This is temporary - not production-ready
- Clearly mark it as example/prototype code
- Replace with proper error handling (`?`, `match`, etc.) before shipping

Use `unwrap()` to explore ideas quickly, but refactor before production.


## Borrowed Strings in Functions Pattern

What is the advantage of this function signature and what types can call it?
```rust
fn validate_email(email: &str) -> bool {
    email.contains('@') && email.contains('.')
}
```

---

The function accepts &str, making it flexible - it works with both String and &str:
```rust
let s = String::from("user@example.com");
validate_email(&s);                    // Works with String
validate_email("user@example.com");    // Works with &str literal
```
This flexibility allows callers to pass any string type without forcing conversions or ownership transfers.


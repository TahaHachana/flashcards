## C-Style Enums with Values

How do you create C-style enums with explicit numeric values in Rust?

---

Assign explicit values to variants:

```rust
enum HttpStatus {
    Ok = 200,
    NotFound = 404,
    InternalServerError = 500,
}

// Cast to integer
let code = HttpStatus::Ok as i32;  // 200
```

**Limitations**:
- Can only use integer types
- Can't easily convert back from integer to enum (need custom implementation)
- Less common in Rust than data-carrying enums

**Use when**: You need numeric constants with type safety, like HTTP status codes, error codes, or protocol values.


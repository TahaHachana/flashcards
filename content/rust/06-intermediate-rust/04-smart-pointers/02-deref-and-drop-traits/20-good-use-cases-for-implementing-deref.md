## Good Use Cases for Implementing Deref

What are three good use cases for implementing `Deref`?

---

**1. Smart pointers:**
```rust
struct MyBox<T>(T);

impl<T> Deref for MyBox<T> {
    type Target = T;
    fn deref(&self) -> &T { &self.0 }
}
```

**2. Newtype pattern for type safety:**
```rust
struct Email(String);

impl Deref for Email {
    type Target = str;
    fn deref(&self) -> &str { &self.0 }
}

// Email has String/str methods but is a distinct type
// Can't pass String where Email is expected
```

**3. Wrapper types with single field:**
```rust
struct SanitizedInput(String);

impl Deref for SanitizedInput {
    type Target = str;
    fn deref(&self) -> &str { &self.0 }
}
```

**Common theme:** The type is pointer-like or a thin wrapper around a single inner value. The deref relationship is obvious and intuitive.


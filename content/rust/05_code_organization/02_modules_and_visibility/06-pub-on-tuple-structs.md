## Pub on Tuple Structs

How does `pub` work with tuple structs, and what's the difference between `pub Email(String)` and `pub Email(pub String)`?

---

**Same rules as regular structs** - the type and its fields are separately controlled.

**Examples**:
```rust
pub struct Email(String);           
// Email is public, inner String is private
// Can create, but can't access .0

pub struct UserId(pub u64);         
// Both UserId and the u64 are public
// Can create and access .0
```

**Usage**:
```rust
let email = Email("user@example.com".to_string());
// email.0;  // ERROR - field is private

let id = UserId(42);
println!("{}", id.0);  // OK - field is public
```


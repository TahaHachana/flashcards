# Tuple Structs

What are tuple structs and how are they defined and used?

---

Tuple structs are like named tuples: they give a distinct type name to a tuple without naming individual fields. They are useful for:
- Creating separate types that would otherwise share the same underlying field types (type safety)
- Lightweight wrappers (e.g., newtype-like patterns with multiple fields)
- Semantic clarity while keeping positional access

```rust
// Defining two tuple structs with identical inner types:
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

let black = Color(0, 0, 0);
let origin = Point(0, 0, 0);

// They are different types; the following would not compile:
// let c: Color = origin; // type mismatch

// Access by pattern matching (destructuring):
let Point(x, y, z) = origin;
println!("origin coords = ({x}, {y}, {z})");

// Index-style access is NOT supported (e.g., origin.0 is valid but only because
// tuple struct fields are positional like tuple elements).
println!("Red component of black: {}", black.0);
```

Key points:
- Field positions (0,1,2,...) act like tuple indices.
- You cannot mix instances of different tuple struct types even if their field types match.
- Derive traits (e.g., Debug, Copy) just like with regular structs.
- Prefer a regular struct when field names improve readability; use tuple structs when names would be redundant (e.g., `struct Inches(u32);`).
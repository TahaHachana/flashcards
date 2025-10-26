## Tuple Struct Definition and Use

What are tuple structs, when should you use them, and how do you access their fields?

---

Tuple structs have a type name but no field names:

```rust
struct Color(u8, u8, u8);
struct Point(f64, f64, f64);

let black = Color(0, 0, 0);
let origin = Point(0.0, 0.0, 0.0);
```

**When to use**:
- Creating distinct types from tuples
- When field names would be redundant
- Creating "newtype" patterns

**Access fields** using numeric indices:
```rust
let red = black.0;
let green = black.1;
```

Even with identical fields, different tuple struct types are incompatible.


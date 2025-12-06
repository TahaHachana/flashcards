## When Deref Coercion Doesn't Happen

In what contexts does deref coercion work, and when doesn't it work?

---

**✅ Works:**

**Function arguments:**
```rust
fn takes_str(s: &str) { }
takes_str(&my_string);  // &String coerced to &str
```

**Method calls:**
```rust
my_string.len();  // String doesn't have len(), but &str does
```

**Explicit type annotation:**
```rust
let s: &str = &my_string;  // Coercion happens
```

**❌ Doesn't work:**

**Assignment without type annotation:**
```rust
let s = &my_string;  // Type is &String, NOT &str
// No coercion without explicit type
```

**Deref coercion only happens in specific contexts** where the compiler knows the expected type. Without type information, no coercion occurs.


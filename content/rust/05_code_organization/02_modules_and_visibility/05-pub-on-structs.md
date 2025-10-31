## Pub on Structs - Fields Are Separate

When you make a struct `pub`, what happens to its fields, and how do you control field visibility?

---

**Rule**: `pub struct` makes the struct name public, but fields remain private unless individually marked `pub`.

**Example**:
```rust
pub struct Person {
    pub name: String,    // Public field - accessible
    age: u32,            // Private field - not accessible
    ssn: String,         // Private field - not accessible
}

impl Person {
    pub fn new(name: String, age: u32) -> Self {
        Self { name, age, ssn: String::new() }
    }
    
    pub fn get_age(&self) -> u32 {
        self.age  // Controlled access via method
    }
}
```

**Benefit**: You control how fields are accessed and can enforce invariants through methods.


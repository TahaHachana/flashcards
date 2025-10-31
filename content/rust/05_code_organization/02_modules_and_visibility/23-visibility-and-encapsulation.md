## Visibility and Encapsulation

How does Rust's visibility system enable encapsulation? Provide a concrete example.

---

**Encapsulation**: Hiding internal details and exposing only controlled interfaces.

**Example - Enforcing Invariants**:
```rust
pub struct Temperature {
    kelvin: f64,  // Private - ensures validity
}

impl Temperature {
    pub fn from_celsius(celsius: f64) -> Result<Self, String> {
        let kelvin = celsius + 273.15;
        if kelvin < 0.0 {
            Err("Temperature below absolute zero".to_string())
        } else {
            Ok(Self { kelvin })
        }
    }
    
    pub fn as_celsius(&self) -> f64 {
        self.kelvin - 273.15
    }
}
```

**Benefits**:
- Can't create invalid temperatures (below absolute zero)
- All conversions go through controlled methods
- Internal representation (`kelvin`) can change without breaking users
- Business rules are enforced automatically

**This is why Rust defaults to private** - encourages deliberate API design.


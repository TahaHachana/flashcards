## Encapsulation with Methods

How do methods enable encapsulation in Rust?

---

Methods provide controlled access to private data:

```rust
pub struct BankAccount {
    balance: f64,  // Private field
}

impl BankAccount {
    pub fn new() -> Self {
        BankAccount { balance: 0.0 }
    }
    
    // Read-only access
    pub fn balance(&self) -> f64 {
        self.balance
    }
    
    // Validated mutation
    pub fn deposit(&mut self, amount: f64) -> Result<(), String> {
        if amount <= 0.0 {
            return Err(String::from("Invalid amount"));
        }
        self.balance += amount;
        Ok(())
    }
}
```

**Benefits**:
- Private fields prevent direct access
- Methods validate inputs
- Maintain invariants (balance never goes negative)
- Can change internal representation without breaking API
- Users interact through a clean public interface


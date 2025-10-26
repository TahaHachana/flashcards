## Getter and Setter Patterns

What are the Rust conventions for getter and setter methods, and why use them?

---

**Getter conventions**:
```rust
impl BankAccount {
    // For Copy types - return the value
    pub fn balance(&self) -> f64 {
        self.balance
    }
    
    // For non-Copy types - return a reference
    pub fn owner(&self) -> &str {
        &self.owner
    }
}
```

**Setter conventions** (with validation):
```rust
impl BankAccount {
    pub fn deposit(&mut self, amount: f64) -> Result<(), String> {
        if amount <= 0.0 {
            return Err(String::from("Amount must be positive"));
        }
        self.balance += amount;
        Ok(())
    }
}
```

**Why use them**:
- Control access to private fields
- Validate inputs
- Maintain invariants
- Can change internal representation without breaking API


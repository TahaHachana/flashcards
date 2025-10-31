## Public Struct with Private Fields Pattern

Why would you make a struct public but keep its fields private? Show an example.

---

**Reason**: Control how fields are accessed and modified, enforcing invariants through methods.

**Example**:
```rust
pub struct BankAccount {
    balance: f64,  // Private - can't directly modify
}

impl BankAccount {
    pub fn new(initial: f64) -> Self {
        Self { balance: initial }
    }
    
    pub fn deposit(&mut self, amount: f64) {
        if amount > 0.0 {  // Enforce rule: no negative deposits
            self.balance += amount;
        }
    }
    
    pub fn withdraw(&mut self, amount: f64) -> Result<(), String> {
        if amount > self.balance {
            Err("Insufficient funds".to_string())
        } else {
            self.balance -= amount;
            Ok(())
        }
    }
}
```

**Benefit**: Users can't break rules (like negative balance) because they can't access `balance` directly.


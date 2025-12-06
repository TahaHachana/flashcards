## Benefits of Implementing Deref

What three main benefits do you get from implementing `Deref` for a type?

---

**1. Access to the target type's methods:**
```rust
impl Deref for HoldsANumber {
    type Target = u8;
    fn deref(&self) -> &Self::Target { &self.0 }
}

my_number.checked_sub(100);  // u8 method available
my_number.pow(2);            // Another u8 method
```

**2. You can still add your own custom methods:**
```rust
impl HoldsANumber {
    fn print_doubled(&self) {
        println!("{}", self.0 * 2);
    }
}

my_number.checked_sub(100);  // From u8 via Deref
my_number.print_doubled();   // Our own method
```

**3. Ergonomic use in function calls:**
```rust
fn takes_u8_ref(n: &u8) { }

let my_number = HoldsANumber(20);
takes_u8_ref(&my_number);  // Works via deref coercion!
```


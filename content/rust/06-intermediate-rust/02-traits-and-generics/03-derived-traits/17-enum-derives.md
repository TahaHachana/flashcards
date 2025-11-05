## Deriving for Enums

Can you derive traits for enums? How does it work?

---

Yes! Enums can derive the same traits as structs. The generated code handles each variant appropriately:

```rust
#[derive(Debug, Clone, PartialEq)]
enum Status {
    Pending,
    Active { start_time: u64 },
    Completed { duration: u64 },
}

fn main() {
    let s1 = Status::Active { start_time: 100 };
    let s2 = s1.clone();  // Works!
    println!("{:?}", s1);  // Debug output
    assert!(s1 == s2);     // Comparison
}
```

The derived implementations work across all variants.


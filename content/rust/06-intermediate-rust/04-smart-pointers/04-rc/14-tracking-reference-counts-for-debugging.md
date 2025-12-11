## Tracking Reference Counts for Debugging

How do you debug `Rc` usage by tracking strong and weak counts? Provide a debugging helper.

---

```rust
use std::rc::Rc;

// Helper function to print counts
fn print_counts<T>(name: &str, rc: &Rc<T>) {
    println!(
        "{}: strong={}, weak={}",
        name,
        Rc::strong_count(rc),
        Rc::weak_count(rc)
    );
}

fn main() {
    let data = Rc::new(String::from("data"));
    print_counts("Initial", &data);
    // Initial: strong=1, weak=0
    
    let weak = Rc::downgrade(&data);
    print_counts("After weak", &data);
    // After weak: strong=1, weak=1
    
    let data2 = Rc::clone(&data);
    print_counts("After clone", &data);
    // After clone: strong=2, weak=1
    
    drop(data2);
    print_counts("After drop", &data);
    // After drop: strong=1, weak=1
}
```

**Debugging tips:**
- Strong count should match expected number of owners
- If count never decreases, you may have a leak
- If count is higher than expected, check for unintended clones
- Use `Rc::ptr_eq()` to check if two Rc's point to same data

**Finding leaks:**
```rust
// Count should eventually return to 1 or 0
if Rc::strong_count(&data) > expected {
    println!("Possible leak or cycle!");
}
```


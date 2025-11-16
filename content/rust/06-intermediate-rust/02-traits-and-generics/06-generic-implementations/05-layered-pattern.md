## Layered Implementation Pattern

What is the "layered implementation" pattern and why is it useful?

---

Layered implementation provides progressively more functionality as types implement more traits:

```rust
struct DataStore<T> {
    data: Vec<T>,
}

// Base layer: methods for any T
impl<T> DataStore<T> {
    fn new() -> Self { DataStore { data: Vec::new() } }
    fn add(&mut self, item: T) { self.data.push(item); }
}

// Layer 2: when T: Clone
impl<T: Clone> DataStore<T> {
    fn duplicate_all(&self) -> Vec<T> {
        self.data.clone()
    }
}

// Layer 3: when T: Display
impl<T: Display> DataStore<T> {
    fn print_all(&self) {
        for item in &self.data {
            println!("{}", item);
        }
    }
}
```

**Benefit**: Types automatically gain capabilities as they implement more traits.


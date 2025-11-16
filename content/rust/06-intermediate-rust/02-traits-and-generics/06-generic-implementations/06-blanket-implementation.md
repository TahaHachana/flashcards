## Blanket Implementation

What is a blanket implementation and how does it work?

---

A blanket implementation implements a trait for all types (or all types meeting certain criteria):

```rust
trait Printable {
    fn print(&self);
}

// Blanket impl: ALL types with Display get Printable
impl<T: Display> Printable for T {
    fn print(&self) {
        println!("{}", self);
    }
}

fn main() {
    42.print();           // i32 implements Display, gets Printable
    "hello".print();      // &str implements Display, gets Printable
}
```

**Use case**: Automatically provide traits to many types at once. The standard library uses this extensively (e.g., `Display` → `ToString`).


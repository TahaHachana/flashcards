## What Is Monomorphization?

What is monomorphization and how does it work?

---

**Monomorphization** is the process where the compiler generates specialized versions of generic functions for each concrete type used.

```rust
fn print<T: Display>(value: T) {
    println!("{}", value);
}

fn main() {
    print(42);        // T = i32
    print("hello");   // T = &str
}

// Compiler generates (conceptually):
// fn print_i32(value: i32) { println!("{}", value); }
// fn print_str(value: &str) { println!("{}", value); }
```

**Result**: Each type gets its own optimized, direct-call version. This is why generics have zero runtime cost but increase binary size.


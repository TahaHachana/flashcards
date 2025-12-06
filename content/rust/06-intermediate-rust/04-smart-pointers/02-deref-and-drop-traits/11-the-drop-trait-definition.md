## The Drop Trait Definition

What is the `Drop` trait signature, and what is its purpose?

---

```rust
pub trait Drop {
    fn drop(&mut self);
}
```

**Purpose:** Customize what happens when a value goes out of scope. It's Rust's version of a destructor.

**Key characteristics:**
- Single method: `drop(&mut self)`
- Called automatically when value goes out of scope
- Cannot be called manually directly (use `std::mem::drop()` instead)

**Example:**
```rust
struct CustomPointer {
    data: String,
}

impl Drop for CustomPointer {
    fn drop(&mut self) {
        println!("Dropping: {}", self.data);
    }
}

fn main() {
    let c = CustomPointer {
        data: String::from("my stuff"),
    };
}  // c.drop() called automatically here
```

Drop enables RAII (Resource Acquisition Is Initialization) pattern in Rust.


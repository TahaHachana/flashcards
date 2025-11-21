## Combining Static and Dynamic Dispatch

How can you effectively combine static and dynamic dispatch?

---

Use both approaches where each makes sense:

```rust
// Generic function for type-safe API (static dispatch)
fn process_shape<T: Shape>(shape: &T) {
    println!("Area: {}", shape.area());
    println!("Perimeter: {}", shape.perimeter());
}

// Trait object for heterogeneous storage (dynamic dispatch)
fn process_all(shapes: &[Box<dyn Shape>]) {
    for shape in shapes {
        println!("Area: {}", shape.area());
    }
}

// Use type parameter for flexibility, trait object for storage
fn register_and_process<T: Plugin + 'static>(
    registry: &mut PluginRegistry,
    plugin: T
) {
    registry.add(Box::new(plugin));  // Store as trait object
}
```

This gets benefits of both: type safety + heterogeneous collections.


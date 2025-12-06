## Deref Trait in Smart Pointers

What does implementing the `Deref` trait enable for smart pointers? Provide an example of deref coercion.

---

Implementing `Deref` enables:
1. Using the `*` operator to access the inner value
2. Automatic dereferencing in method calls (deref coercion)
3. Treating the smart pointer "like" the data it contains

Example of deref coercion:
```rust
fn print_str(s: &str) {
    println!("{}", s);
}

let boxed_string = Box::new(String::from("hello"));
print_str(&boxed_string);  // Box<String> automatically derefs to &str
```

The compiler automatically converts `&Box<String>` → `&String` → `&str` through deref coercion.


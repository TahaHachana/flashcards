## What is Deref Coercion?

What is deref coercion, and provide an example showing how `&String` automatically converts to `&str`.

---

**Deref coercion** is Rust's automatic conversion between reference types by calling `.deref()` as many times as needed.

Example:
```rust
fn print_str(s: &str) {
    println!("{}", s);
}

fn main() {
    let my_string = String::from("hello");
    print_str(&my_string);  // &String automatically converts to &str
}
```

**How it works:**
1. Compiler sees `&String` where `&str` is expected
2. Checks if `String` implements `Deref`
3. Finds `impl Deref for String { type Target = str; }`
4. Automatically calls `.deref()` to convert `&String` to `&str`

This makes smart pointers ergonomic - you can pass them to functions expecting references to the inner type.


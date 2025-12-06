## Chained Deref Coercion

Explain how chained deref coercion works with an example involving `Rc<String>` being passed to a function expecting `&str`.

---

Deref coercion can chain through multiple types:

```rust
use std::rc::Rc;

fn print_str(s: &str) {
    println!("{}", s);
}

fn main() {
    let rc_string = Rc::new(String::from("hello"));
    print_str(&rc_string);  // Works!
}
```

**Deref chain:**
1. Start with `&Rc<String>`
2. `Rc` implements `Deref<Target = String>` → `&String`
3. `String` implements `Deref<Target = str>` → `&str`
4. Function receives `&str`

Rust automatically follows the chain: `&Rc<String>` → `&String` → `&str`

Each step calls `.deref()` on the previous result until reaching the expected type.


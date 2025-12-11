## Why Rc Exists - The Ownership Problem

What ownership problem does `Rc` solve? Provide an example showing the problem and solution.

---

Rust's ownership rules say every value has **one owner**, but sometimes multiple parts of code need to own the same data.

**The problem:**
```rust
fn takes_a_string(_s: String) { }

fn main() {
    let name = String::from("Alice");
    takes_a_string(name);
    takes_a_string(name);  // ❌ Error: value already moved!
}
```

**Traditional solutions:**
- Clone: `takes_a_string(name.clone())` - expensive for large data
- References: `&name` - lifetime complexity

**Rc solution:**
```rust
use std::rc::Rc;

fn takes_a_string(_s: Rc<String>) { }

fn main() {
    let name = Rc::new(String::from("Alice"));
    takes_a_string(Rc::clone(&name));  // ✅ Works!
    takes_a_string(Rc::clone(&name));  // ✅ Works!
}
```

`Rc` allows multiple ownership without cloning the actual data - only the pointer is cloned.


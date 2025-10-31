## Making Functions Public

What happens if you forget to add `pub` to a function in a module?

---

The function remains **private** and cannot be accessed from outside the module.

**Example**:
```rust
mod utils {
    fn helper() {}  // Private function
}

fn main() {
    utils::helper();  // ERROR: function `helper` is private
}
```

**Solution**:
```rust
mod utils {
    pub fn helper() {}  // Now public
}

fn main() {
    utils::helper();  // OK!
}
```

The compiler will give a clear error message showing where the private item is defined.


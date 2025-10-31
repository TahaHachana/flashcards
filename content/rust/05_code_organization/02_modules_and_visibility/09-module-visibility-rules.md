## Module Visibility Rules

What are the visibility rules for top-level vs nested modules?

---

**Top-level modules** (in crate root):
- Public within their crate by default
- Need `pub` to be accessible from other crates

**Nested modules**:
- Private by default
- Need `pub` to be accessible from outside their parent module

**Example**:
```rust
mod network {                    // Public within crate
    pub mod server {             // Must be pub
        pub fn start() {}
    }
    
    mod client {                 // Private
        fn connect() {}
    }
}

fn main() {
    network::server::start();    // OK
    // network::client::connect(); // ERROR - private
}
```


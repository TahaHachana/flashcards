## Pattern 2 Configuration Objects

What characterizes the configuration/context object pattern with lifetimes?

---

Multiple borrowed fields (references) with the same lifetime, often mixed with owned fields. The lifetime constrains when the struct can exist—it must not outlive the referenced configuration data. Example:
```rust
struct Config<'a> {
    app_name: &'a str,
    version: &'a str,
    debug: bool,  // owned field
}
```
All references typically share one lifetime `'a`.


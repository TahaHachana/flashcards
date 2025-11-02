## Lifetime Syntax Basics

What is the syntax for declaring and using a lifetime parameter in a function signature?

---

Lifetimes are declared with angle brackets after the function name and used with the `&` reference operator:
```rust
fn function_name<'a>(param: &'a Type) -> &'a Type
```
The `<'a>` declares a generic lifetime parameter (like `<T>` for types), and `&'a Type` indicates a reference with lifetime `'a`. The lifetime name must be declared before it can be used.


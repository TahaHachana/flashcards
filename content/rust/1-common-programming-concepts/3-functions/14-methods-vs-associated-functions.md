## Methods vs Associated Functions

What is the difference between a method and an associated function?

---

* A **method** takes `self` (or `&self`, `&mut self`) as its first parameter and is called on an instance.
* An **associated function** does not take `self` and is called with the type name (often used as constructors).

Example:

```rust
impl Circle {
    fn area(&self) -> f64 { 3.14 * self.r * self.r }
    fn new(r: f64) -> Circle { Circle { r } }
}
```


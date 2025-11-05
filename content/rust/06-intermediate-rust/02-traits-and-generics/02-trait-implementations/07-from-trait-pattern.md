## From Trait Pattern

What does implementing the `From` trait give you, and what's the syntax?

---

Implementing `From<T>` for your type allows conversion from type T to your type. You automatically get `Into<YourType>` for free.

```rust
struct Fahrenheit(f64);
struct Celsius(f64);

impl From<Celsius> for Fahrenheit {
    fn from(c: Celsius) -> Self {
        Fahrenheit(c.0 * 9.0/5.0 + 32.0)
    }
}

// Can now use:
let f = Fahrenheit::from(Celsius(100.0));
// or:
let f: Fahrenheit = Celsius(100.0).into();
```


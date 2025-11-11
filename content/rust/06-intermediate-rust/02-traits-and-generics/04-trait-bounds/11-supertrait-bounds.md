## Supertrait Bounds

What is a supertrait bound and how does it work?

---

A supertrait bound means a trait requires another trait. Any type implementing the trait must also implement its supertrait:

```rust
trait Printable: Display {  // Printable requires Display
    fn print_fancy(&self) {
        println!(">>> {} <<<", self);  // Can use Display
    }
}

fn use_printable<T: Printable>(item: T) {
    // T automatically has Display because Printable requires it
    println!("{}", item);
    item.print_fancy();
}
```

The syntax `trait Printable: Display` means "to implement Printable, you must first implement Display."


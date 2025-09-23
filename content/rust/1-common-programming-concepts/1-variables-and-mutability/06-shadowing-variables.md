## Shadowing Variables

What is variable shadowing in Rust?

---

Shadowing occurs when a new variable with the same name as an existing one is declared using `let`.
The new variable overrides the previous one within its scope.
Often used for step-by-step transformations without introducing new names.

```rust
fn main() {
    let x = 5;
    let x = x + 1; // shadows previous x
    {
        let x = x * 2; // shadows again in inner scope
        println!("inner x = {x}"); // 12
    }
    println!("outer x = {x}"); // 6
}
```


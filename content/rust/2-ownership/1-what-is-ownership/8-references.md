# References and Borrowing

What are references and why use them?

---

References (`&T` or `&mut T`) allow borrowing data without taking ownership, avoiding moves and extra returns.

```rust
fn calculate_length(s: &String) -> usize {
    s.len()
}

let s = String::from("hello");
let len = calculate_length(&s);
println!("Length: {}", len); // s still valid
```
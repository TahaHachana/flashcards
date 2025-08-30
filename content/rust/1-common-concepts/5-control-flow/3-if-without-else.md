# If Without Else

What happens if the `if` condition is false and there is no `else` block?

---

The `if` block is skipped and execution continues with the next statement.

```rust
fn main() {
    let number = 7;
    if number < 5 {
        println!("Less than 5");
    }
    println!("This always runs");
}
```
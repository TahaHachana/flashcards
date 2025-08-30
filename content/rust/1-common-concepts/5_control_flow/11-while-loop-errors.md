# While Loop Errors

Why is looping through a collection with `while` potentially error-prone?

---

Manual index management can cause out-of-bounds errors or missed elements.

```rust
fn main() {
    let arr = [1, 2, 3];
    let mut i = 0;
    while i < arr.len() {
        println!("{}", arr[i]);
        i += 1;
    }
}
```
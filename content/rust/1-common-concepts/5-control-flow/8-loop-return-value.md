# Loop Return Value

How can you return a value from a `loop`?

---

Use `break` followed by the value.

```rust
fn main() {
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 3 {
            break counter * 2;
        }
    };
    println!("result = {result}");
}
```
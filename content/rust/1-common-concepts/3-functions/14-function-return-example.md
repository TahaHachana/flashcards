# Function Return Example

What does this function return?
```rust
fn example() -> i32 {
    let x = 5;
    let y = {
        let z = 3;
        z + 1
    };
    x + y
}
```

---

Returns `9`. The block assigns `4` to `y` (since `z + 1` = `4`), then the final expression `x + y` = `5 + 4` = `9`.
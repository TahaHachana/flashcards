## Function Scope

Are variables declared inside a function accessible outside it?

---

No. Variables declared inside functions are local to that function.

```rust
fn example() {
    let x = 5;
}
fn main() {
    println!("{}", x);  // ❌ Error: x doesn't exist here
}
```


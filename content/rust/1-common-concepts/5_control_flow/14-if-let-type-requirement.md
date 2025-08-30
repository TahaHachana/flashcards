# If Let Type Requirement

What is the key requirement when using `if` in a `let` statement?

---

All branches must evaluate to the same type.

```rust
fn main() {
    let condition = true;
    // let x = if condition { 5 } else { "six" }; // ❌ type mismatch
    let x = if condition { 5 } else { 6 }; // ✅ both i32
    println!("{x}");
}
```
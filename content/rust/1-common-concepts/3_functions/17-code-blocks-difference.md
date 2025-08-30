# Code Blocks Difference

What's the difference between these two code blocks?
```rust
// Block A
{
    let x = 3;
    x + 1;
}

// Block B  
{
    let x = 3;
    x + 1
}
```

---

- **Block A**: Returns `()` because `x + 1;` is a statement (has semicolon)
- **Block B**: Returns `4` because `x + 1` is an expression (no semicolon)

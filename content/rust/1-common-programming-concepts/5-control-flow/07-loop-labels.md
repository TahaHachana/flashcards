## Loop Labels

How do loop labels work in Rust?

---

Loop labels let you `break` or `continue` a specific loop when nested.

```rust
'outer: loop {
    loop {
        break 'outer; // exits the outer loop
    }
}
```


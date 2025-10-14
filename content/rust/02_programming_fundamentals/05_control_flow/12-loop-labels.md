## Loop Labels

How do you break out of an outer loop from within a nested loop?

---

Use loop labels starting with a single quote.

```rust
'outer: loop {
    loop {
        break 'outer;  // Breaks the outer loop
    }
}
```


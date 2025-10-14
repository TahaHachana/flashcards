## Returning Values from loop

How can a loop return a value?

---

Place the value after break.

```rust
let result = loop {
    counter += 1;
    if counter == 10 {
        break counter * 2;  // Returns 20
    }
};
```


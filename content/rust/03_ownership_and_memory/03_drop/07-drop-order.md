## Drop Order

In what order are values dropped?

---

Reverse order of creation (LIFO - last in, first out). Later variables might depend on earlier ones, so dropping in reverse ensures dependencies are valid.

```rust
let first = String::from("1st");
let second = String::from("2nd");
// Dropped: second, then first
```


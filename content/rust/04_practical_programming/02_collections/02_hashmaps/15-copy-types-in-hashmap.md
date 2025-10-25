## Copy Types in HashMap

What's the difference in ownership when using Copy types (i32) vs non-Copy types (String) as HashMap keys?

---

**Copy types**: Values are copied, originals remain usable
```rust
let k = 1;
map.insert(k, 10);
println!("{}", k); // OK
```

**Non-Copy types**: Values are moved, originals become invalid
```rust
let k = String::from("key");
map.insert(k, 10);
// println!("{}", k); // ERROR: k was moved
```


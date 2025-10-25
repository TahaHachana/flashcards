## Mutable Slice Exclusivity

Can you access the original collection while a mutable slice exists?

---

No. Exclusive mutable access - can't access original while mutable slice exists.

```rust
let slice = &mut vec[1..4];
println!("{:?}", vec);  // ❌ Error
slice[0] = 10;
```


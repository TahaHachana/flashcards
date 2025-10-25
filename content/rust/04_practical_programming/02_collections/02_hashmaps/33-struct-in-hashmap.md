## Struct in HashMap

Can you store structs as HashMap values? What about as keys?

---

**As values**: Yes, always possible
```rust
HashMap<String, Player>
```

**As keys**: Only if struct implements `Eq` and `Hash`
```rust
#[derive(Eq, PartialEq, Hash)]
struct PlayerId(u32);

HashMap<PlayerId, Player>
```


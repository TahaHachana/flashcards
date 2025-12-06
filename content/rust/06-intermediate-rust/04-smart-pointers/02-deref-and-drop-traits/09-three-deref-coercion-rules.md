## Three Deref Coercion Rules

What are the three cases where Rust will automatically perform deref coercion?

---

**1. From `&T` to `&U` when `T: Deref<Target=U>`**
```rust
let s = String::from("hello");
let str_ref: &str = &s;  // &String -> &str
```

**2. From `&mut T` to `&mut U` when `T: DerefMut<Target=U>`**
```rust
let mut s = String::from("hello");
let str_ref: &mut str = &mut s;  // &mut String -> &mut str
```

**3. From `&mut T` to `&U` when `T: Deref<Target=U>`**
```rust
let mut s = String::from("hello");
let str_ref: &str = &mut s;  // &mut String -> &str (mutable to immutable)
```

**Important:** You **cannot** coerce `&T` to `&mut U` (immutable to mutable). This would violate Rust's borrowing rules.


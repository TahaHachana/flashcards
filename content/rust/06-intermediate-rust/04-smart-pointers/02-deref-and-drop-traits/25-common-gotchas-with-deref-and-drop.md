## Common Gotchas with Deref and Drop

What are four common gotchas when working with `Deref` and `Drop`?

---

**Gotcha 1: Can't call .drop() directly**
```rust
let s = String::from("hello");
// s.drop();  // ❌ Error!
drop(s);      // ✅ Use std::mem::drop instead
```

**Gotcha 2: DerefMut requires Deref**
```rust
// ❌ Can't implement DerefMut without Deref
impl DerefMut for MyType { ... }  // Error!

// ✅ Must implement Deref first
impl Deref for MyType { ... }
impl DerefMut for MyType { ... }
```

**Gotcha 3: Deref coercion doesn't work everywhere**
```rust
let s = String::from("hello");
let r = &s;           // Type: &String (no coercion)
let r: &str = &s;     // Type: &str (coercion with annotation)
```

**Gotcha 4: Move prevents drop**
```rust
let x = Loud;
let y = x;  // x moved
// x.drop() NOT called - only y.drop() called
```

Understanding these gotchas prevents common mistakes and confusion.


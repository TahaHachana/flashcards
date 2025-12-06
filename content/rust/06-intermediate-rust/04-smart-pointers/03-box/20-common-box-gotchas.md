## Common Box Gotchas

What are three common gotchas when working with `Box`?

---

**Gotcha 1: Box doesn't implement Copy**
```rust
let b1 = Box::new(5);
let b2 = b1;  // Move, not copy
// println!("{}", b1);  // ❌ Error! b1 was moved

// Use clone if you need a copy
let b1 = Box::new(5);
let b2 = b1.clone();  // ✅ Explicit copy
```

**Gotcha 2: Can't create Box of unsized type directly**
```rust
trait Animal { }
struct Dog;

// ❌ Can't box trait directly
// let boxed: Box<dyn Animal> = Dog;

// ✅ Must use Box::new
let boxed: Box<dyn Animal> = Box::new(Dog);
```

**Gotcha 3: Box<[T]> vs Box<[T; N]> size difference**
```rust
// Box<[i32; 3]>: 8 bytes (just pointer)
let array_box: Box<[i32; 3]> = Box::new([1, 2, 3]);

// Box<[i32]>: 16 bytes (pointer + length)
let slice_box: Box<[i32]> = vec![1, 2, 3].into_boxed_slice();
```

Understanding these prevents common mistakes and confusion.


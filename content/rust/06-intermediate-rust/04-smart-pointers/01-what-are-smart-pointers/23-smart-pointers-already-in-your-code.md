## Smart Pointers Already in Your Code

Name three types you've been using that are actually smart pointers, and explain what makes each one a smart pointer.

---

**1. `String` (smart pointer to `str`):**
- **Owns**: Heap-allocated string data
- **Metadata**: Length and capacity
- **Deref**: `Deref<Target = str>` allows `&String` → `&str`
```rust
let s = String::from("hello");
print_str(&s);  // Works due to deref coercion
```

**2. `Vec<T>` (smart pointer to `[T]`):**
- **Owns**: Heap-allocated array data
- **Metadata**: Length and capacity
- **Deref**: `Deref<Target = [T]>` allows `&Vec<T>` → `&[T]`
```rust
let v = vec![1, 2, 3];
print_slice(&v);  // Works due to deref coercion
```

**3. `Box<T>` (smart pointer to `T`):**
- **Owns**: Heap-allocated value of type `T`
- **Metadata**: None (just a pointer)
- **Deref**: `Deref<Target = T>` allows `&Box<T>` → `&T`
```rust
let b = Box::new(42);
let value = *b;  // Deref to get i32
```

You've been using smart pointers since your first `String` or `Vec`!


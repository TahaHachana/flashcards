## Box and Deref Coercion

How does `Box<T>` use deref coercion, and what does this enable?

---

`Box<T>` implements `Deref<Target = T>`, allowing automatic conversion from `&Box<T>` to `&T`.

**Example:**
```rust
fn takes_i32_ref(n: &i32) {
    println!("{}", n);
}

fn main() {
    let boxed = Box::new(42);
    
    // All these work due to Deref:
    takes_i32_ref(&boxed);      // &Box<i32> -> &i32
    println!("{}", *boxed);     // Dereference to i32
    println!("{}", boxed + 10); // Automatic deref in expression
}
```

**What this enables:**
1. **Transparent use:** Box acts like the value it contains
2. **Ergonomic APIs:** Pass Box where `&T` is expected
3. **Method access:** Call `T`'s methods on `Box<T>`

**Under the hood:**
```rust
impl<T> Deref for Box<T> {
    type Target = T;
    fn deref(&self) -> &T {
        // Returns reference to heap data
    }
}
```

**Benefit:** You can mostly forget you're working with a Box and treat it like the inner value.


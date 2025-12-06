## Transparent Wrapper Pattern

Demonstrate the transparent wrapper pattern using `Deref` and `DerefMut`.

---

```rust
use std::ops::{Deref, DerefMut};

struct Wrapper<T>(T);

impl<T> Deref for Wrapper<T> {
    type Target = T;
    fn deref(&self) -> &T { 
        &self.0 
    }
}

impl<T> DerefMut for Wrapper<T> {
    fn deref_mut(&mut self) -> &mut T { 
        &mut self.0 
    }
}

// Now Wrapper<T> acts transparently like T
fn main() {
    let mut wrapped = Wrapper(vec![1, 2, 3]);
    
    // Can call Vec methods directly
    wrapped.push(4);           // Via DerefMut
    println!("{}", wrapped.len());  // Via Deref
    
    // Can pass to functions expecting Vec
    fn takes_vec(v: &Vec<i32>) { }
    takes_vec(&wrapped);  // Works!
}
```

**Purpose:** Add functionality to existing types while maintaining transparent access to the wrapped value.


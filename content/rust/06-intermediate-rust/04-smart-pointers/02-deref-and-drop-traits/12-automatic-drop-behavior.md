## Automatic Drop Behavior

Explain the automatic drop process. What happens when a value goes out of scope?

---

**When a value goes out of scope:**

```rust
fn main() {
    {
        let s = String::from("hello");
        // Use s
    }  // <- s goes out of scope and is dropped here
    
    // s is no longer accessible
}
```

**What happens during drop:**
1. Rust calls `s.drop()` if `Drop` is implemented
2. Recursively drops all fields
3. Deallocates the memory

**Every value in Rust is automatically dropped** - you don't need to manually free memory. This is how Rust achieves memory safety without garbage collection.

**Drop order:** Variables are dropped in **reverse order of creation** (LIFO - Last In, First Out).

```rust
let a = DebugDrop { name: "a" };
let b = DebugDrop { name: "b" };
let c = DebugDrop { name: "c" };
// Drops: c, then b, then a
```


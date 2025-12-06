## Drop Order in Structs and Functions

Explain the drop order for variables in a function and fields in a struct.

---

**Variables in a function - Reverse order (LIFO):**
```rust
fn main() {
    let a = DebugDrop { name: "a" };
    let b = DebugDrop { name: "b" };
    let c = DebugDrop { name: "c" };
}
// Output: Dropping: c, Dropping: b, Dropping: a
```

Variables drop in **reverse order of creation** - last created, first dropped.

**Fields in a struct - Declaration order:**
```rust
struct Container {
    first: DebugDrop,
    second: DebugDrop,
}

impl Drop for Container {
    fn drop(&mut self) {
        println!("Dropping Container");
        // Then fields drop in declaration order:
        // 1. first
        // 2. second
    }
}
```

Fields drop in the **order they're declared** in the struct definition.

**Why it matters:** Understanding drop order is crucial for managing resources that depend on each other.


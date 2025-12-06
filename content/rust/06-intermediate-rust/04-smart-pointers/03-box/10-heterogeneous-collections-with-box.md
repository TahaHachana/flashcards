## Heterogeneous Collections with Box

How do you store different types implementing the same trait in a single collection? Provide an example.

---

Use `Vec<Box<dyn Trait>>` to store different types in one collection:

```rust
trait Draw {
    fn draw(&self);
}

struct Circle { radius: f64 }
impl Draw for Circle {
    fn draw(&self) { println!("Drawing circle"); }
}

struct Square { side: f64 }
impl Draw for Square {
    fn draw(&self) { println!("Drawing square"); }
}

fn main() {
    // ✅ Can store different types that implement Draw
    let shapes: Vec<Box<dyn Draw>> = vec![
        Box::new(Circle { radius: 5.0 }),
        Box::new(Square { side: 10.0 }),
        Box::new(Circle { radius: 3.0 }),
    ];
    
    for shape in shapes.iter() {
        shape.draw();
    }
}
```

**Output:**
```
Drawing circle
Drawing square
Drawing circle
```

**Key insight:** Without `Box<dyn Trait>`, you can't store different concrete types in the same Vec.


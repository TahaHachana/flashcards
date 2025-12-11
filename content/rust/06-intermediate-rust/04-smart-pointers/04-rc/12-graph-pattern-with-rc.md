## Graph Pattern with Rc

Demonstrate how to use `Rc` to implement a graph where multiple nodes can point to the same neighbor.

---

```rust
use std::rc::Rc;

struct Node {
    value: i32,
    edges: Vec<Rc<Node>>,
}

fn main() {
    // Create shared node
    let node1 = Rc::new(Node {
        value: 1,
        edges: vec![],
    });
    
    // Multiple nodes point to node1
    let node2 = Rc::new(Node {
        value: 2,
        edges: vec![Rc::clone(&node1)],
    });
    
    let node3 = Rc::new(Node {
        value: 3,
        edges: vec![Rc::clone(&node1)],
    });
    
    println!("node1 count: {}", Rc::strong_count(&node1));  // 3
    
    // node1 is shared by node2 and node3
}
```

**Why Rc is needed:**
- Multiple nodes need to "own" the same neighbor
- Can't use references (lifetime complexity)
- Don't want to clone the entire node (expensive)
- Rc allows cheap shared ownership

**Pattern:** Common in graphs, DAGs, and any structure with shared nodes.


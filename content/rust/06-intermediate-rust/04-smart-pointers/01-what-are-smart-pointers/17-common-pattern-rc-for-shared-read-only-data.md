## Common Pattern - Rc for Shared Read-Only Data

Describe the common pattern of using `Rc<T>` for shared read-only data with an example.

---

`Rc<T>` is ideal when multiple parts of your program need read access to the same data without mutation.

**Example: Graph structure**
```rust
use std::rc::Rc;

struct Node {
    value: i32,
    neighbors: Vec<Rc<Node>>,  // Multiple nodes point to same neighbor
}

fn main() {
    let node1 = Rc::new(Node {
        value: 1,
        neighbors: vec![],
    });
    
    let node2 = Node {
        value: 2,
        neighbors: vec![Rc::clone(&node1)],  // Shares node1
    };
    
    let node3 = Node {
        value: 3,
        neighbors: vec![Rc::clone(&node1)],  // Also shares node1
    };
    
    // node1 is shared by both node2 and node3
}
```

This pattern is common in: graphs, trees with parent pointers, DAGs, caches.


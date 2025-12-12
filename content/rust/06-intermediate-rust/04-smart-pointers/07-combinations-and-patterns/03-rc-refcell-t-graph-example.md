## Rc<RefCell<T>> Graph Example

Demonstrate using `Rc<RefCell<T>>` to build a graph where nodes can have multiple neighbors and connections can be added after creation.

---

```rust
use std::rc::Rc;
use std::cell::RefCell;

struct Node {
    value: i32,
    neighbors: RefCell<Vec<Rc<Node>>>,
}

impl Node {
    fn new(value: i32) -> Rc<Self> {
        Rc::new(Node {
            value,
            neighbors: RefCell::new(vec![]),
        })
    }
    
    fn add_neighbor(&self, neighbor: Rc<Node>) {
        self.neighbors.borrow_mut().push(neighbor);
    }
}

fn main() {
    let node1 = Node::new(1);
    let node2 = Node::new(2);
    let node3 = Node::new(3);
    
    // Create graph connections
    node1.add_neighbor(Rc::clone(&node2));
    node1.add_neighbor(Rc::clone(&node3));
    node2.add_neighbor(Rc::clone(&node1));  // Bidirectional
    
    println!("Node 1 has {} neighbors", 
             node1.neighbors.borrow().len());
}
```

**Why Rc<RefCell<T>>?**
- Multiple nodes reference same neighbor → `Rc`
- Neighbor lists change after creation → `RefCell`
- Graph is single-threaded → Not `Arc`/`Mutex`

**Breaking down the layers:**
```
Rc<Node>
│
└─ neighbors: RefCell<Vec<Rc<Node>>>
              │          │
              │          └─ Multiple nodes point to same neighbor
              └─ Can modify neighbor list through &self
```


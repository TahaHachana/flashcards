## Graph with Bidirectional References

Demonstrate using `Rc<RefCell<T>>` to create a graph with bidirectional connections.

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
    
    fn connect(&self, other: &Rc<Node>) {
        // Add other to self's neighbors
        self.neighbors.borrow_mut().push(Rc::clone(other));
        // Add self to other's neighbors
        other.neighbors.borrow_mut().push(Rc::clone(&Rc::new(self.clone())));
    }
}

fn main() {
    let node1 = Node::new(1);
    let node2 = Node::new(2);
    
    // Create bidirectional connection
    node1.neighbors.borrow_mut().push(Rc::clone(&node2));
    node2.neighbors.borrow_mut().push(Rc::clone(&node1));
    
    println!("Node 1 has {} neighbors", 
             node1.neighbors.borrow().len());
}
```

**Pattern breakdown:**
- `Rc`: Multiple nodes can point to same neighbor
- `RefCell`: Can modify neighbor list through shared reference
- Together: Build complex graph structures safely


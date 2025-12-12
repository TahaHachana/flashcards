## Pattern Selection Example - UI Tree

Walk through choosing the right smart pointer pattern for a UI component tree. What are the requirements and what pattern fits?

---

**Requirements:**
- Components reference each other (parent/children)
- Components need to update state
- Single-threaded (UI runs on main thread)
- Tree structure changes dynamically

**Decision process:**
```
Need multiple owners? 
└─ Yes (parent and children reference same components)
    └─ Single or multi-threaded?
        └─ Single-threaded (UI thread)
            └─ Need mutability?
                └─ Yes (update state, modify tree)
                    └─ Pattern: Rc<RefCell<T>>
```

**Implementation:**
```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct Component {
    id: String,
    children: RefCell<Vec<Rc<Component>>>,
    parent: RefCell<Weak<Component>>,
    state: RefCell<State>,
}

impl Component {
    fn update_state(&self, new_state: State) {
        *self.state.borrow_mut() = new_state;
    }
    
    fn add_child(&self, child: Rc<Component>) {
        *child.parent.borrow_mut() = Rc::downgrade(&Rc::new(self.clone()));
        self.children.borrow_mut().push(child);
    }
}
```

**Why this pattern:**
- `Rc`: Multiple components reference same child
- `RefCell`: State and tree structure change
- `Weak`: Parent pointer prevents cycles
- Not `Arc`: UI is single-threaded


## Combining Three Smart Pointers

Can you combine more than two smart pointers? Show an example and explain when this might be needed.

---

Yes, you can nest multiple smart pointers when you need multiple capabilities.

**Example: Shared trait object with interior mutability**
```rust
use std::rc::Rc;
use std::cell::RefCell;

trait Component {
    fn update(&mut self);
}

struct Button {
    label: String,
}

impl Component for Button {
    fn update(&mut self) {
        self.label = "Clicked".to_string();
    }
}

// Three layers
type SharedComponent = Rc<RefCell<Box<dyn Component>>>;

fn main() {
    let component: SharedComponent = Rc::new(
        RefCell::new(
            Box::new(Button {
                label: "Click me".to_string(),
            })
        )
    );
    
    let component2 = Rc::clone(&component);
    
    // Can mutate through either reference
    component.borrow_mut().update();
}
```

**Breaking down the layers:**
```
Rc<RefCell<Box<dyn Component>>>
│    │       │
│    │       └─ Box: Trait object (dynamic dispatch)
│    └─ RefCell: Interior mutability
└─ Rc: Shared ownership
```

**When needed:**
- Multiple owners → `Rc`
- Interior mutability → `RefCell`
- Trait object → `Box<dyn Trait>`

**Caution:** More layers = more complexity. Use only when all three capabilities genuinely needed.


## Observable Pattern with Rc<RefCell<T>>

Implement an observable pattern using `Rc<RefCell<T>>` where observers are notified when a value changes.

---

```rust
use std::rc::Rc;
use std::cell::RefCell;

type Observer = Rc<dyn Fn(i32)>;

struct Observable {
    value: RefCell<i32>,
    observers: RefCell<Vec<Observer>>,
}

impl Observable {
    fn new(value: i32) -> Self {
        Observable {
            value: RefCell::new(value),
            observers: RefCell::new(vec![]),
        }
    }
    
    fn subscribe(&self, observer: Observer) {
        self.observers.borrow_mut().push(observer);
    }
    
    fn set(&self, new_value: i32) {
        *self.value.borrow_mut() = new_value;
        
        // Notify all observers
        for observer in self.observers.borrow().iter() {
            observer(new_value);
        }
    }
    
    fn get(&self) -> i32 {
        *self.value.borrow()
    }
}

fn main() {
    let observable = Observable::new(0);
    
    observable.subscribe(Rc::new(|v| {
        println!("Observer 1 sees: {}", v);
    }));
    
    observable.subscribe(Rc::new(|v| {
        println!("Observer 2 sees: {}", v);
    }));
    
    observable.set(10);  // Both observers notified
}
```

**Why Rc<RefCell<T>>:**
- Observers shared by value and observer list → `Rc`
- Value and list modified through `&self` → `RefCell`
- Single-threaded event system → Not `Arc`


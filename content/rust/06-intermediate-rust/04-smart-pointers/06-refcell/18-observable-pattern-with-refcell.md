## Observable Pattern with RefCell

Implement an observable pattern using `RefCell` where observers are notified when a value changes.

---

```rust
use std::rc::Rc;
use std::cell::RefCell;

struct Observable {
    value: RefCell<i32>,
    observers: RefCell<Vec<Rc<dyn Fn(i32)>>>,
}

impl Observable {
    fn new(value: i32) -> Self {
        Observable {
            value: RefCell::new(value),
            observers: RefCell::new(vec![]),
        }
    }
    
    fn subscribe(&self, observer: Rc<dyn Fn(i32)>) {
        self.observers.borrow_mut().push(observer);
    }
    
    fn set(&self, new_value: i32) {
        *self.value.borrow_mut() = new_value;
        self.notify(new_value);
    }
    
    fn notify(&self, value: i32) {
        for observer in self.observers.borrow().iter() {
            observer(value);
        }
    }
}

fn main() {
    let observable = Observable::new(0);
    
    observable.subscribe(Rc::new(|v| {
        println!("Observer 1: {}", v);
    }));
    
    observable.subscribe(Rc::new(|v| {
        println!("Observer 2: {}", v);
    }));
    
    observable.set(10);  // Both observers notified
    // Output:
    // Observer 1: 10
    // Observer 2: 10
}
```

**Why RefCell:**
- Subscribe and set take `&self`, not `&mut self`
- Need to mutate internal collections
- Single-threaded event system


## Box<dyn Trait> Pattern

When do you use `Box<dyn Trait>` and why? Provide an example.

---

**When to use:**
- Need dynamic dispatch
- Different types implementing same trait
- Size not known at compile time
- Single ownership (not sharing)

**Example: Plugin System**
```rust
trait Plugin {
    fn execute(&self);
}

struct AudioPlugin;
impl Plugin for AudioPlugin {
    fn execute(&self) {
        println!("Playing audio");
    }
}

struct VideoPlugin;
impl Plugin for VideoPlugin {
    fn execute(&self) {
        println!("Playing video");
    }
}

fn main() {
    let plugins: Vec<Box<dyn Plugin>> = vec![
        Box::new(AudioPlugin),
        Box::new(VideoPlugin),
    ];
    
    for plugin in plugins {
        plugin.execute();
    }
}
```

**Why Box<dyn Trait>:**
- Different plugin types in same collection
- Dynamic dispatch (runtime method lookup)
- Each plugin owned by vector
- Size known (pointer + vtable pointer)

**Alternatives:**
- `Rc<dyn Trait>` - Shared ownership (single-threaded)
- `Arc<dyn Trait>` - Shared ownership (multi-threaded)


## Plugin System Pattern

How do trait objects enable plugin systems?

---

Trait objects allow loading and running plugins of different types at runtime:

```rust
trait Plugin {
    fn name(&self) -> &str;
    fn execute(&self);
}

struct PluginManager {
    plugins: Vec<Box<dyn Plugin>>,
}

impl PluginManager {
    fn register(&mut self, plugin: Box<dyn Plugin>) {
        self.plugins.push(plugin);
    }
    
    fn run_all(&self) {
        for plugin in &self.plugins {
            println!("Running: {}", plugin.name());
            plugin.execute();
        }
    }
}
```

Different plugin types can be registered and run through the same interface.


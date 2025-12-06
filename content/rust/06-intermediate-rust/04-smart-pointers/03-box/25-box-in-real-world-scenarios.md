## Box in Real-World Scenarios

Provide three real-world scenarios where `Box` is the right choice, with brief examples.

---

**1. Parser/Compiler AST (Abstract Syntax Trees):**
```rust
enum ASTNode {
    Number(i32),
    BinaryOp {
        op: Operation,
        left: Box<ASTNode>,   // Recursive structure
        right: Box<ASTNode>,
    },
}
// Enables recursive tree structures for code representation
```

**2. Plugin System:**
```rust
trait Plugin {
    fn execute(&self);
}

fn load_plugins() -> Vec<Box<dyn Plugin>> {
    vec![
        Box::new(AudioPlugin),
        Box::new(VideoPlugin),
        // Different plugin types in one collection
    ]
}
```

**3. Large Configuration Structs:**
```rust
struct AppConfig {
    // Avoid stack overflow with large config
    database: Box<DatabaseConfig>,  // 1000s of bytes
    cache: Box<CacheConfig>,        // 1000s of bytes
    network: Box<NetworkConfig>,    // 1000s of bytes
}
// Keeps stack frame small while allowing large configs
```

**Common thread:** Box enables patterns that would be impossible or problematic otherwise.


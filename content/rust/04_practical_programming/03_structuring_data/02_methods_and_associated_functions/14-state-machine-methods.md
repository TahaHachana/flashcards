## State Machine Pattern with Methods

How can you use methods with consuming self to implement a type-safe state machine?

---

Use generic types and consuming methods to enforce valid transitions:

```rust
struct Connection<State> {
    address: String,
    state: State,
}

struct Disconnected;
struct Connected;

impl Connection<Disconnected> {
    fn new(address: String) -> Self {
        Connection { address, state: Disconnected }
    }
    
    fn connect(self) -> Connection<Connected> {
        Connection {
            address: self.address,
            state: Connected,
        }
    }
}

impl Connection<Connected> {
    fn send_data(&self, data: &str) { }
    
    fn disconnect(self) -> Connection<Disconnected> {
        Connection {
            address: self.address,
            state: Disconnected,
        }
    }
}
```

The compiler enforces that you can only call methods valid for the current state.


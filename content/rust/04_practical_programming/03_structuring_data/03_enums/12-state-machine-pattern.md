## State Machine Pattern with Enums

Why are enums ideal for modeling state machines? Provide a simple example.

---

Enums are perfect for state machines because:
- Each state is a variant
- Each state can carry relevant data
- Compiler ensures all states are handled
- Type system enforces valid transitions

```rust
enum ConnectionState {
    Disconnected,
    Connecting,
    Connected { session_id: u64 },
    Error { reason: String },
}

struct Connection {
    state: ConnectionState,
}

impl Connection {
    fn connect(&mut self) {
        match self.state {
            ConnectionState::Disconnected => {
                self.state = ConnectionState::Connecting;
            }
            _ => println!("Already connecting/connected"),
        }
    }
}
```

Each state carries only the data relevant to that state.


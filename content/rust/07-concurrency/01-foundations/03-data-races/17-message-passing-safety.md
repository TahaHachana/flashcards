## Message Passing Safety

Why is message passing through channels (mpsc::channel) safe from data races?

---

Channels transfer ownership of data from sender to receiver. When you send data, ownership is moved into the channel, and when you receive it, ownership is moved to the receiver. Only one thread owns the data at any time. This breaks the "multiple threads accessing same memory" condition - there's no shared access because ownership is transferred, not shared. The type system enforces this by requiring sent data to be Send.


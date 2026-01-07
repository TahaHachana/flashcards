## Box Dyn Any Send Meaning

Why is the panic payload type Box<dyn Any + Send>? Explain each component.

---

Box: heap-allocated because payload size is unknown at compile time. dyn Any: trait object allowing runtime type inspection and downcasting to concrete types. Send: ensures payload can cross thread boundaries (required because join() transfers it between threads). This type allows panics to carry any Send type while maintaining type safety and thread safety. Most commonly contains &str or String but can be any Send type.


## Extracting Panic Messages

How do you extract the panic message from a thread panic error?

---

Use downcast_ref on the panic payload to try converting it to &str or String. Pattern: if let Some(s) = e.downcast_ref::<&str>() { /* use s */ } else if let Some(s) = e.downcast_ref::<String>() { /* use s */ }. Most panics carry &str or String messages, but the payload can be any Send type. The Any trait allows runtime type inspection to extract the actual message type.


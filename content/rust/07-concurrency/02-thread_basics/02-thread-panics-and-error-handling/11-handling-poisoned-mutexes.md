## Handling Poisoned Mutexes

What are the three ways to handle a poisoned mutex?

---

(1) Propagate error: mutex.lock()? passes PoisonError to caller. (2) Panic: mutex.lock().unwrap() panics if poisoned. (3) Recover: match mutex.lock() { Ok(guard) => use guard, Err(poisoned) => poisoned.into_inner() } accesses data anyway. Choose based on whether the data corruption matters for your use case. Sometimes the data is still valid despite the panic.


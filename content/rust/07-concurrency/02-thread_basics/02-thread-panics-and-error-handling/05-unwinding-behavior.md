## Unwinding Behavior

What is unwinding, and in what order are destructors called during a panic?

---

Unwinding is the process of walking back up the stack when a panic occurs, calling destructors for all local variables. Destructors are called in reverse order (LIFO) - the most recently created variables are dropped first. This ensures proper cleanup: resources acquired later are released before resources acquired earlier. Unwinding maintains the RAII (Resource Acquisition Is Initialization) pattern even during failures.


## Join Result Type

What is the return type of join(), and what does each variant represent?

---

join() returns Result<T, Box<dyn Any + Send>> where: Ok(T) contains the thread's return value if it completed successfully, and Err(Box<dyn Any + Send>) contains the panic payload if the thread panicked. T is the return type of the thread's closure. The Box<dyn Any + Send> can contain any Send type, typically a &str or String panic message, and allows runtime type inspection.


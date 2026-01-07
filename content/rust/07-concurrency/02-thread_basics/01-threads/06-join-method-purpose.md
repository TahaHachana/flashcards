## Join Method Purpose

What does the join() method do, and what does it return?

---

join() blocks the current thread until the spawned thread completes. It returns Result<T, Box<dyn Any + Send>> where: Ok(T) contains the thread's return value if it completed successfully, or Err(e) contains the panic payload if the thread panicked. Calling join consumes the JoinHandle - you can only join a thread once. It's how you wait for a thread and get its result.


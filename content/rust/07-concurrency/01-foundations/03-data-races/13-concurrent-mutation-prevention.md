## Concurrent Mutation Prevention

Why doesn't this compile: `let mut counter = 0; thread::spawn(|| { counter += 1; }); counter += 1;`?

---

Both the spawned thread and parent thread would mutate counter without synchronization, causing a data race. Rust's borrowing rules prevent capturing mutable references in closures that might outlive the scope. The closure can't capture &mut counter because the borrow would need to last as long as the thread (potentially forever). The compiler prevents this at compile time, forcing you to use proper synchronization like Mutex.


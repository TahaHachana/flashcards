## Multiple Threads Pattern

What's the common pattern for managing multiple threads?

---

Collect JoinHandles in a Vec: spawn threads in a loop pushing handles to the vector, then iterate the vector calling join() on each handle to wait for all threads and collect results. This ensures all threads complete and their results/errors are handled. Pattern: let mut handles = vec![]; for ... { handles.push(thread::spawn(...)); } for handle in handles { handle.join().unwrap(); }


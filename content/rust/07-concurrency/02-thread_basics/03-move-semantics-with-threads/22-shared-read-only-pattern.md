## Shared Read Only Pattern

How do you share read-only data across multiple threads efficiently?

---

Use Arc to wrap the data, clone the Arc for each thread, move each Arc clone into its thread. Pattern: let data = Arc::new(vec![1,2,3]); for thread in threads { let data = Arc::clone(&data); spawn(move || read from data); }. All threads have read access, no cloning of actual data, minimal overhead (atomic reference counting). The data is immutable so no synchronization needed beyond Arc's reference counting.


## Parallel Map Pattern

How do you implement parallel map using move semantics?

---

Split data into chunks, clone each chunk, move each chunk into a thread that processes it and returns results, collect all results. Pattern: for chunk in chunks { let chunk_copy = chunk.to_vec(); handles.push(thread::spawn(move || process(chunk_copy))); } then join all and combine results. Each thread gets its own data copy (independent processing), processes in parallel, returns results that are merged.


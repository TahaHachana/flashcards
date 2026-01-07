## Ownership Transfer Back

Can ownership transfer back from thread to parent, and how?

---

Yes, through the thread's return value. The thread owns data (via move), returns it when done, parent receives it through join(). Pattern: let handle = spawn(move || { process data; data }); let data = handle.join().unwrap();. Ownership flows: parent → thread (via move) → parent (via return). This allows the thread to work with exclusive ownership then return the result. Common for parallel computation.


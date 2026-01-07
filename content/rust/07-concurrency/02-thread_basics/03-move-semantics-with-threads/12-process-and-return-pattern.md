## Process and Return Pattern

Describe the process and return pattern for threads.

---

Move data into thread, process it, return the result. Pattern: let handle = thread::spawn(move || { process(data); result }); let result = handle.join().unwrap();. The thread owns the data, does computation, and returns the result via the return value. Parent gets result through join(). Useful for parallel computation where you send work to a thread and get back the answer.


## Supervisor Pattern

What is the supervisor pattern for thread management?

---

A parent thread monitors worker threads and restarts them if they panic. Check if worker thread has finished with is_finished(), join to check for panic, spawn replacement if it panicked. Common in long-running services where workers handle tasks from a queue - if a worker panics on a bad task, supervisor restarts it to continue processing. Erlang/OTP inspired pattern for fault tolerance.


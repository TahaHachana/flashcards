## Timeout with Panic Handling

How do you implement timeout handling that also catches thread panics?

---

Spawn thread with time-limited operation, have main thread wait for a duration, then check if thread is finished. Use join() to detect both completion and panics. Pattern: spawn thread with slow work, main sleeps for timeout duration, join with is_finished() check. If not finished, you know it timed out. If finished, join tells you if it succeeded or panicked. Handles both timeout (thread alive too long) and panic (thread failed).


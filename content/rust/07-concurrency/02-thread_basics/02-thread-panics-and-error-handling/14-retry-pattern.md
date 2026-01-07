## Retry Pattern

Describe the retry pattern for handling thread failures.

---

Wrap thread spawning in a loop with max attempts. On failure (join returns Err), retry the operation. Pattern: for attempt in 0..max_attempts { match spawn_and_join() { Ok(result) => { use result; break; } Err(_) => { log retry; if last attempt { give up }}}}. Useful for transient failures, network operations, or resource contention. Set reasonable retry limits to avoid infinite loops.


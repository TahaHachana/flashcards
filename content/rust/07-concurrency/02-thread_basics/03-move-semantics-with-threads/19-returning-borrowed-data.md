## Returning Borrowed Data

Why can't you return borrowed data from a thread: `thread::spawn(|| &data[0])`?

---

The thread would return a reference to data that might be dropped. The parent scope (where data lives) could end before the thread returns, making the reference invalid. Threads require 'static or ownership, so returned references must point to 'static data. Fix: return owned values (data[0] instead of &data[0]), or use Arc to ensure data lives long enough, or return indices instead of references.


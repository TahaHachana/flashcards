## Why Cell Is Not Sync

Why is Cell<T> not Sync, and what would happen if it were?

---

Cell<T> provides interior mutability without synchronization - it allows mutation through shared references without locking. If multiple threads could access a Cell simultaneously, they could race to read and write, causing data races. For example, one thread reading while another writes could see torn/inconsistent data. The compiler prevents this by making Cell not implement Sync.


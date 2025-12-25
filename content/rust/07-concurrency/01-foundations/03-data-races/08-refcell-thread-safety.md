## RefCell Thread Safety

Why does the compiler prevent sharing RefCell<T> between threads, and what data race would occur if it didn't?

---

RefCell provides interior mutability without synchronization - it allows mutation through shared references with only runtime borrow checking. If multiple threads accessed a RefCell simultaneously, they could race to read and write with no coordination, causing data races. The compiler prevents this by making RefCell not Sync - you can't share &RefCell between threads, forcing you to use Mutex instead.


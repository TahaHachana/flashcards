## Closure Factory Pattern

How do you create closures that capture different data and can be spawned as threads?

---

Create a function that takes data as parameters and returns a closure capturing that data. Pattern: fn make_worker(data: Vec<i32>) -> impl FnOnce() + Send { move || process(data) }. The returned closure owns the data (via move). Each call to make_worker creates a new closure with different captured data. Then spawn each closure: thread::spawn(make_worker(data1)); thread::spawn(make_worker(data2));.


## Use After Free in Threads

Why doesn't this compile: `let data = vec![1,2,3]; thread::spawn(|| { println!("{:?}", &data); }); drop(data);`?

---

The thread might access data after it's dropped, causing use-after-free. Rust's lifetime system ensures borrowed data outlives all references to it, even across thread boundaries. The compiler can't guarantee the thread will finish before data is dropped, so it prevents borrowing data in a thread that might outlive the borrow. You must either move ownership (move) or use Arc for shared ownership.


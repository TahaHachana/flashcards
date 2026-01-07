## Capturing References Error

Why doesn't this compile: `let v = vec![1,2,3]; thread::spawn(|| println!("{:?}", v));`?

---

The closure tries to borrow v, but the thread might outlive the scope where v exists, causing use-after-free. The compiler requires either: (1) move keyword to transfer ownership: thread::spawn(move || ...), or (2) Use scoped threads that guarantee completion before v is dropped. Regular threads require 'static lifetime or ownership because they can outlive their parent scope.


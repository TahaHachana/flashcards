## Borrowing Without Move

Why doesn't this compile without move: `let v = vec![1,2,3]; thread::spawn(|| println!("{:?}", v));`?

---

The closure tries to borrow v, but the thread might outlive the scope where v exists. When the scope ends, v would be dropped, leaving the thread with a dangling reference (use-after-free). The compiler prevents this by requiring either 'static lifetime or ownership via move. Adding move transfers ownership to the thread, making it safe - the thread owns v so it can't be dropped prematurely.


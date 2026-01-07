## Forgetting Move Gotcha

What error occurs if you forget the move keyword when capturing non-Copy types in thread closures?

---

Error: "borrowed value does not live long enough" or "closure may outlive the current function". The closure tries to borrow the variable, but the thread might outlive the scope where it's borrowed from. The compiler prevents this use-after-free at compile time. Fix: add move keyword to transfer ownership. This is a common beginner mistake - the error message points you to use move.


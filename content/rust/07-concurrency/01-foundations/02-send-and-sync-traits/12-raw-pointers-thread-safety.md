## Raw Pointers Thread Safety

Why aren't raw pointers (*const T and *mut T) Send or Sync by default?

---

Raw pointers have no lifetime tracking or safety guarantees. The compiler can't verify that the pointed-to data will remain valid if the pointer is sent to another thread or shared between threads. Without these guarantees, using raw pointers across threads could lead to use-after-free, data races, or accessing freed memory. You must use unsafe and manually guarantee safety if you need to send raw pointers between threads.


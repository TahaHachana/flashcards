## Moving Mutable Data

Can you move mutable data into a thread, and can the thread return it?

---

Yes to both. The thread becomes the owner and can mutate the data freely. The thread can return owned data via its return value, which you get through join(). Pattern: let handle = thread::spawn(move || { data.push(4); data }); let data = handle.join().unwrap();. This transfers ownership from parent to thread, thread modifies it, then transfers ownership back to parent via the return value.


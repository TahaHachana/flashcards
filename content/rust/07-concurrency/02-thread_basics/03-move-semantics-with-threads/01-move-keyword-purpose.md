## Move Keyword Purpose

What does the move keyword do in thread closures, and why is it necessary?

---

The move keyword transfers ownership of captured variables from the parent scope into the thread's closure. It's necessary because threads can outlive their parent scope, so they can't safely borrow data - the borrowed data might be dropped while the thread still needs it. Move makes the thread the sole owner of the data, satisfying the 'static lifetime requirement and preventing data races by ensuring only one thread owns the data.


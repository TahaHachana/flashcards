## Smart Pointer Mental Model - Book Ownership

Explain the book ownership analogy for understanding references vs smart pointers.

---

**Regular Reference (`&T`) - Library Book:**
- Like borrowing a book from a library
- You can read it, but don't own it
- Must return it (can't outlive the borrow)
- Multiple people can borrow to read (multiple `&T`)
- Only one person can borrow to write in it (`&mut T`)

**Smart Pointer (`Box<T>`) - Buying a Book:**
- Like buying your own copy
- You own it completely
- Do whatever you want with it
- It's yours until you discard it (drop)

**Reference Counted (`Rc<T>`) - Co-owned Book:**
- Like co-owning a book with friends
- Everyone has equal access
- Book is only discarded when the last owner gives up their copy
- All owners can read it (shared ownership)


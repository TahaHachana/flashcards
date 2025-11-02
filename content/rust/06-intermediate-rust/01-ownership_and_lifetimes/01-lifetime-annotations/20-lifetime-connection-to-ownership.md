## Lifetime Connection to Ownership

How do lifetimes relate to Rust's ownership system?

---

Ownership determines who is responsible for cleanup, while lifetimes determine how long borrowed data remains valid. Lifetimes enforce that references never outlive what they point to—this is the bridge between ownership (who owns it) and borrowing (who can use it temporarily). Together they ensure memory safety without garbage collection.


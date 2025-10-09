## Use-After-Free Prevention

How does ownership prevent use-after-free bugs?

---

Once ownership is transferred or dropped, the original owner cannot access the value. The compiler enforces that you cannot use memory after it has been freed, making use-after-free impossible at compile time.


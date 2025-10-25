## Initial Vector Capacity

What capacity does a new vector get when you first `.push()` an element? What happens when you exceed capacity?

---

First push gives capacity 4. When capacity is exceeded, Rust allocates new memory with **double the previous capacity** and copies all elements over (reallocation).


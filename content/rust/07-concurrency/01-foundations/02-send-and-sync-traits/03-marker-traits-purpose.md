## Marker Traits Purpose

What are marker traits and what makes Send and Sync marker traits?

---

Marker traits carry no functionality or methods - they exist purely to communicate information to the compiler. Send and Sync are marker traits that tell the compiler about thread safety properties. They don't provide any methods; they just mark types as safe to send between threads (Send) or safe to share between threads (Sync). The compiler uses these markers to enforce thread safety at compile time.


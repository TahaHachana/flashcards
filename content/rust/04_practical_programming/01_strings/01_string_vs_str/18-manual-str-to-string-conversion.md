## Manual &str to String Conversion

When converting from &str to String, does Rust perform automatic conversion? Why or why not?

---

No, &str to String conversion always requires an explicit method call. This is because it must allocate heap memory and copy data, which is an expensive operation. Rust makes you explicit about this cost to prevent accidental performance issues. Use when you need ownership of the string data.


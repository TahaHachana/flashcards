## Standard Library Structs with Lifetimes

What are some examples of standard library types that use lifetime parameters?

---

- `std::str::Chars<'a>`: Iterator over string characters
- `std::slice::Iter<'a, T>`: Iterator over slice elements
- `std::collections::hash_map::Iter<'a, K, V>`: Iterator over HashMap entries

Understanding struct lifetimes helps you use these types. They all hold references to borrowed data and yield items with those lifetimes.


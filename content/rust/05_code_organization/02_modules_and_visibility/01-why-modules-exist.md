## Why Modules Exist in Rust

What are the four main reasons for using modules in Rust?

---

1. **Building your code**: Helps you think about structure and remember where code belongs as projects grow
2. **Avoiding name conflicts**: Different modules can have items with the same name without conflict
3. **Reading your code**: Module paths are self-documenting (e.g., `std::collections::HashMap`)
4. **Privacy and encapsulation**: Keep implementation details private, expose only what users need

Modules create separate namespaces and let you control what's accessible.


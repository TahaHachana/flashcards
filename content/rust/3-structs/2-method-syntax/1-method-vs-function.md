# Method vs Function

What distinguishes a Rust method from a free function?

---

A method is defined inside an impl block with its first parameter named self, and is called using dot syntax on an instance, whereas a free function is defined outside an impl and called by name.
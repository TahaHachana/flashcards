## What Are Lifetime Bounds in Structs?

What problem do lifetime bounds in structs solve, and how do they work?

---

Lifetime bounds solve the problem of storing references in structs that might outlive the data they reference. A struct with lifetime parameter like `struct Excerpt<'a>` creates a contract: "This struct holds a reference to data, that data must live at least as long as I do, therefore I cannot outlive my referenced data." The lifetime parameter `'a` connects the struct's lifetime to its referenced data's lifetime, constraining when instances can exist.


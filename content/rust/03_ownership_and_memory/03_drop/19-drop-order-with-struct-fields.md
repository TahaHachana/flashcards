## Drop Order with Struct Fields

In what order are struct fields dropped?

---

The struct's drop() is called first, then fields are dropped in the order they appear in the struct definition.


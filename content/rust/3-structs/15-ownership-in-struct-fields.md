## Ownership In Struct Fields

How does ownership apply to struct fields?

---

Struct fields follow normal ownership rules.
Moving a field may move ownership out of the struct.
Fields are stored together in memory, making access efficient.


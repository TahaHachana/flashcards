## Auto-Implementation Rules

How does the compiler automatically implement Send and Sync for custom types?

---

The compiler derives Send and Sync based on a type's composition using propagation rules: (1) If all fields are Send, the type is Send, (2) If all fields are Sync, the type is Sync, (3) If any field is not Send, the type is not Send, (4) If any field is not Sync, the type is not Sync. You rarely implement these manually - the compiler does it automatically by examining the fields.


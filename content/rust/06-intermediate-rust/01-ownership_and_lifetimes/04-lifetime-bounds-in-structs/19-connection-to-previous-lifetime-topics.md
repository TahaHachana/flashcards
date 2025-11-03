## Connection to Previous Lifetime Topics

How do the previous three lifetime topics apply to struct methods?

---

- Topic 1 (Annotations): All annotation rules apply to struct methods
- Topic 2 (Patterns): Struct methods follow the same patterns (especially Pattern 3 - methods returning from self)
- Topic 3 (Elision): Rule 3 handles most struct method elision—output defaults to `self`'s lifetime (which is the struct's `'a`)

Everything learned applies, but in the context of structs holding references.


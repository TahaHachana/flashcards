## Bad Use Cases for Implementing Deref

Provide examples of when you should NOT implement `Deref`, and explain why.

---

**Bad: Type isn't pointer-like**
```rust
// ❌ Character isn't a pointer to i8
struct Character {
    name: String,
    hp: i8,
}

impl Deref for Character {
    type Target = i8;
    fn deref(&self) -> &i8 { &self.hp }  // Confusing!
}

let billy = Character { name: "Billy".into(), hp: 100 };
let hp = *billy;  // What?? Character derefs to i8??
```

**Bad: Deref relationship isn't obvious**
```rust
// ❌ Why would Person deref to String?
struct Person {
    name: String,
    age: u32,
}

impl Deref for Person {
    type Target = String;
    fn deref(&self) -> &String { &self.name }
}
```

**Why bad:** Makes code confusing and unintuitive. Readers must search for Deref implementation to understand behavior.

**Better alternatives:** Use methods with clear names like `get_hp()`, `get_name()`.

**Rule:** Only implement Deref for actual smart pointer patterns.


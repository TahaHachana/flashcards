## Unit Tuple Struct Variants

What forms can enum variants take in Rust?

---

Variants can be:

* **Unit-like** (no data): `Quit`
* **Tuple-like** (unnamed values): `Write(String)`
* **Struct-like** (named fields): `Move { x: i32, y: i32 }`


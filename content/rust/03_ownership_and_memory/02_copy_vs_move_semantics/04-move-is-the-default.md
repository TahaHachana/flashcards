## Move is the Default

Which semantics does Rust use by default: copy or move?

---

Move is the default. Unless a type explicitly implements Copy, it uses move semantics. This is the safe default - assume ownership transfer.


## One Owner One Dropper

How does ownership guarantee correct cleanup?

---

Each value has exactly one owner, so Drop is called exactly once when that owner goes out of scope. No leaks (always dropped), no double-frees (only one owner).


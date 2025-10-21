## Drop and Copy Mutual Exclusion

Can a type implement both Drop and Copy?

---

No. They're mutually exclusive. Copy implies bit-wise duplication - if both copies had Drop, both would run cleanup, potentially freeing the same resource twice.


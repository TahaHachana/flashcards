## Why Borrowing Prevents Data Races

How does borrowing prevent data races?

---

Mutable exclusivity rule: only one &mut or multiple &, never both. Prevents concurrent modification that could cause unpredictable behavior.


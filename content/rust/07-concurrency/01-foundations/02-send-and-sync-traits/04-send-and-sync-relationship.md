## Send and Sync Relationship

What is the relationship between Send and Sync? Complete this statement: "T is Sync if and only if..."

---

T is Sync if and only if &T is Send. This means: if you can safely share references to T between threads (T is Sync), then you can safely send those references to other threads (so &T is Send). Conversely, if &T is not Send, then T cannot be Sync. The two traits are fundamentally connected through this relationship.


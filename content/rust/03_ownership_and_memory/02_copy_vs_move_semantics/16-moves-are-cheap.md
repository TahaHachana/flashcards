## Moves Are Cheap

What is the performance cost of moving ownership?

---

Very cheap - just copying a few bytes on the stack (pointer, length, capacity). The heap data isn't copied. The old variable is invalidated.


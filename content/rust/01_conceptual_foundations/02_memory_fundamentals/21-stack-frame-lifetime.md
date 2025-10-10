## Stack Frame Lifetime

What happens to all local variables when a function returns?

---

The entire stack frame is popped off instantly. All local stack variables disappear automatically in one operation. This is why stack memory doesn't need manual cleanup or garbage collection.


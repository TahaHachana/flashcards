## Clone Before Move

When should you clone data before moving it into a thread, and what are the trade-offs?

---

Clone when: both the thread and parent need the data, you want independent copies that don't affect each other, or you want to avoid synchronization overhead. Trade-offs: Benefits - no synchronization needed, modifications are independent, simpler than Arc. Costs - duplicates data (memory), cloning takes time, changes in one copy don't affect others. Use clone for independent work, Arc for sharing.


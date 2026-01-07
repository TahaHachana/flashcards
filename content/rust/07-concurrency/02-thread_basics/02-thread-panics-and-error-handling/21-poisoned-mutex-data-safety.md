## Poisoned Mutex Data Safety

Is the data in a poisoned mutex always corrupted, and how should you decide whether to use it?

---

No, poisoned doesn't mean corrupted - it means potentially inconsistent. The panicking thread may have completed its modifications or may have left data mid-update. Decision factors: (1) Was the operation atomic or multi-step? (2) Can you validate the data? (3) What are consequences of using bad data? Sometimes data is fine (panic was unrelated), sometimes it's unsafe. Use into_inner() only when you've determined it's safe for your specific use case.


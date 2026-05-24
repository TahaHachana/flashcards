## Single Point of Failure in CVCS

What is the critical weakness of a Centralized VCS (CVCS)?

---

A CVCS has a **single point of failure**: if the central server goes down, no one can collaborate or access history. If the central disk is corrupted with no backups, the **entire project history is permanently lost**. Every client only has the latest snapshot, not the full history.


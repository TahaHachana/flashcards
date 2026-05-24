## Local Operations Speed

Why is Git extremely fast for most operations compared to a CVCS?

---

Because Git mirrors the **entire repository history locally**, nearly every operation only requires local disk access — no network round-trips needed. This includes browsing history, comparing versions, and switching branches. Operations that would take seconds over a network are instantaneous locally.

